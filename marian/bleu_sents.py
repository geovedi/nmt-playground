#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import fire
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

def main(ref, hyp, out):
    smoothing_func = SmoothingFunction()
    with io.open(out, 'w', encoding='utf-8') as out_f, \
         io.open(ref, 'r', encoding='utf-8') as ref_f, \
         io.open(hyp, 'r', encoding='utf-8') as hyp_f:
        for ref_s, hyp_s in zip(ref_f, hyp_f):
            score = sentence_bleu(
                [ref_s.strip().split()],
                hyp_s.split(),
                smoothing_function=smoothing_func.method4)
            out_f.write('{0:0.4f}\n'.format(score))

if __name__ == '__main__':
    fire.Fire(main)
