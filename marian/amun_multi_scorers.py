#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import io
import threading
import fire
from subprocess import Popen, PIPE, DEVNULL, TimeoutExpired
from collections import defaultdict
from pyaml import yaml
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu


def extract_ngrams(sent, max_len):
    res = defaultdict(lambda: defaultdict(int))
    for ln in range(max_len):
        for start in range(len(sent)):
            end = start + ln + 1
            if end <= len(sent):
                res[ln][tuple(sent[start:end])] += 1
    return res


def get_correct(ngrams_ref, ngrams_hyp, max_len):
    correct = [0] * max_len
    total = [0] * max_len
    for r in ngrams_hyp:
        for c in ngrams_hyp[r]:
            total[r] += ngrams_hyp[r][c]
            if c in ngrams_ref[r]:
                correct[r] += min(ngrams_hyp[r][c], ngrams_ref[r][c])
    return correct, total


def f1(correct, total_hyp, total_ref, max_len, b=3, smooth=1e-6):
    prec, rec = 0, 0
    for i in range(max_len):
        if total_hyp[i] + smooth and total_ref[i] + smooth:
            prec += (correct[i] + smooth) / (total_hyp[i] + smooth)
            rec += (correct[i] + smooth) / (total_ref[i] + smooth)
    prec /= max_len
    rec /= max_len
    score = (1 + b**2) * (prec * rec) / ((b**2 * prec) + rec)
    return score, prec, rec


def chrF_score(ref, hyp, max_len=6):
    if not ref.strip() or not hyp.strip():
        return 0.0
    ngrams_ref = extract_ngrams(ref, max_len)
    ngrams_hyp = extract_ngrams(hyp, max_len)
    correct, total = get_correct(ngrams_ref, ngrams_hyp, max_len)
    total_ref = [0] * max_len
    for r in ngrams_ref:
        for c in ngrams_ref[r]:
            total_ref[r] += ngrams_ref[r][c]
    score, prec, rec = f1(correct, total, total_ref, max_len)
    return score


class Amun(object):
    def __init__(self, name, config, timeout=5):
        self.name = name
        self.config = config
        self.timeout = timeout
        cmd = 'amun -c {0}'.format(config).split()
        self.proc = Popen(
            cmd,
            stdin=PIPE,
            stdout=PIPE,
            stderr=DEVNULL,
            bufsize=1,
            encoding='utf-8',
            universal_newlines=True)
        self.lock = threading.Lock()

    def translate(self, text):
        text = text.strip()
        if self.proc is None:
            return text
        if text is None:
            return ''
        result = text
        with self.lock:
            self.proc.stdin.write(text + '\n')
            self.proc.stdin.flush()
            result = self.proc.stdout.readline()
        return result.strip()


def compute_scores(translators, source, target, sctype='BLEU'):
    if sctype == 'BLEU':
        smoothing_func = SmoothingFunction()
    with io.open(source, 'r', buffering=1, encoding='utf-8') as sources, \
         io.open(target, 'r', buffering=1, encoding='utf-8') as targets:
        for src, tgt in zip(sources, targets):
            sent_scores = []
            for translator in translators:
                hyp = translator.translate(src)
                if sctype == 'CHRF':
                    score = chrF_score(tgt.strip(), hyp)
                else:
                    score = sentence_bleu(
                        [tgt.strip().split()],
                        hyp.split(),
                        smoothing_function=smoothing_func.method4)
                sent_scores.append(score)
            yield sent_scores


def main(config, source, target, output, sctype='BLEU'):
    config = yaml.load(io.open(config, 'r', encoding='utf-8'))

    translators = []
    for model, model_config in config['models'].items():
        translators.append(Amun(model, model_config))

    with io.open(output, 'w', buffering=1) as out:
        scores = compute_scores(translators, source, target, sctype=sctype)
        for sent_scores in scores:
            score_text = ' '.join('{0:0.8f}'.format(s) for s in sent_scores)
            out.write('{0}\n'.format(score_text))


if __name__ == '__main__':
    fire.Fire(main)
