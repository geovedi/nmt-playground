#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import io
import random
import threading
import fire
from subprocess import Popen, PIPE, DEVNULL, TimeoutExpired
from collections import defaultdict
from pyaml import yaml
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


class MarianMT(object):
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


def main(config,
         source,
         target,
         L1,
         L2,
         min_score=0.25,
         max_score=0.75,
         corpus_ratio=0.3):
    src_L1_fname = '{0}.{1}'.format(source, L1)
    src_L2_fname = '{0}.{1}'.format(source, L2)
    tgt_L1_fname = '{0}.{1}'.format(target, L1)
    tgt_L2_fname = '{0}.{1}'.format(target, L2)

    mt = MarianMT('marian-en2id', config)
    smoothing_func = SmoothingFunction()

    with io.open(src_L1_fname, 'r', encoding='utf-8') as src_L1, \
         io.open(src_L2_fname, 'r', encoding='utf-8') as src_L2, \
         io.open(tgt_L1_fname, 'w', buffering=1, encoding='utf-8') as tgt_L1, \
         io.open(tgt_L2_fname, 'w', buffering=1, encoding='utf-8') as tgt_L2:

        pair_no = 0
        for sent_no, (s, t) in enumerate(zip(src_L1, src_L2)):
            if sent_no % 10000 == 0:
                logging.info(
                    'Collected {0} from {1} sentences.'
                    .format(pair_no, sent_no))

            if random.random() > corpus_ratio:
                continue

            try:
                st = mt.translate(s)
                score = sentence_bleu(
                    [t.strip().split()],
                    st.split(),
                    smoothing_function=smoothing_func.method4)

                if min_score <= score <= max_score and random.random():
                    tgt_L1.write(s)
                    tgt_L2.write(t)
                    pair_no += 1

            except Exception as e:
                logging.error('[sent_{0}]: {1}.'.format(sent_no, e))


if __name__ == '__main__':
    fire.Fire(main)
