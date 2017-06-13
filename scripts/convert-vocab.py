#!/usr/bin/env python3

import io
import json
import fire
from collections import OrderedDict


def main(input, output):
    vocab = OrderedDict({'</s>': 0, '<unk>': 1})
    for line in io.open(input, 'r', encoding='utf-8'):
        word, count = line.strip().split()
        vocab[word] = len(vocab)
    with io.open(output, 'w', encoding='utf-8') as out:
        json.dump(vocab, out, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    fire.Fire(main)
