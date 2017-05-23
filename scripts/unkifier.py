# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io
import copy
import math
import fire
import string
import random
from collections import defaultdict

s_join = ' '.join


def get_single_pairs(a):
    m = defaultdict(list)
    for p in a.split():
        i, j = p.split('-')
        m[int(i)].append(int(j))
    for k, v in list(m.items()):
        if len(v) == 1:
            m[k] = v[0]
        else:
            m.pop(k)
    return m


def main(parallel_corpus,
         sentence_aligment,
         score_file,
         source_vocab,
         output_corpus,
         unk='<unk>',
         max_choices=10,
         max_variations=10,
         min_aligment_score=-150.0):
    pcs = io.open(parallel_corpus, 'r', encoding='utf-8')
    als = io.open(sentence_aligment, 'r', encoding='utf-8')
    scr = io.open(score_file, 'r', encoding='utf-8')
    out = io.open(output_corpus, 'w', encoding='utf-8')
    puncts = set(string.punctuation)

    voc = defaultdict(int)
    for line in io.open(source_vocab, 'r', encoding='utf-8'):
        w, c = line.strip().split()
        voc[w] = int(c)

    with pcs, als, out:
        for pc, al, sc in zip(pcs, als, scr):
            try:
                s, t = pc.strip().split(' ||| ')
            except ValueError:
                continue

            if float(sc) < min_aligment_score:
                continue

            s, t = s.split(), t.split()
            amap = get_single_pairs(al)
            unks_main, unks_add = set(), set()

            for i, w in enumerate(s):
                j = amap[i]
                if not j:
                    continue
                if w not in voc:
                    unks_main.add((i, j))
                if w == t[j] and w not in puncts and not w.isdigit():
                    unks_add.add((i, j))

            seen = set()

            cs, ct = copy.deepcopy(s), copy.deepcopy(t)
            for i, j in unks_main:
                cs[i] = unk
                ct[j] = unk
            s_text = s_join(cs)
            t_text = s_join(ct)
            out.write('{0} ||| {1}\n'.format(s_text, t_text))
            seen.add(s_text)

            if not unks_add:
                continue

            unks_add = list(unks_add)
            unks_add_len = len(unks_add)

            for v in range(max_variations):
                cs, ct = copy.deepcopy(s), copy.deepcopy(t)
                for i, j in unks_main:
                    cs[i] = unk
                    ct[j] = unk

                k = random.randint(1, min(max_choices, unks_add_len))
                for i, j in random.choices(unks_add, k=k):
                    cs[i] = unk
                    ct[j] = unk
                    s_text = s_join(cs)
                    t_text = s_join(ct)

                    if s_text in seen:
                        continue

                    out.write(
                        '{0} ||| {1}\n'.format(s_text, t_text))
                    seen.add(s_text)


if __name__ == '__main__':
    fire.Fire(main)
