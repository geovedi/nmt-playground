#!/usr/bin/env python3

import io
import re
import fire
from collections import Counter, defaultdict

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def tokenizer(text, separator='￭'):
  text = re.sub(
      r'(?<=[^\s])([^\w\s{0}])'.format(separator),
      r' {0}\1'.format(separator),
      text,
      flags=re.U)
  text = re.sub(
      r'([^\w\s{0}])(?=[^\s])'.format(separator),
      r'\1{0} '.format(separator),
      text,
      flags=re.U)
  return text.split()


def upper_score(tokens, separator):
    alpha, upper = 0, 0
    for tok in tokens:
        if tok[0].isalpha():
            alpha += 1
        if tok[0].isupper():
            upper += 1
    if alpha == 0:
        return 0.0
    else:
        return upper / alpha


def main(corpus, model, separator='￭', max_sents=10e6):
    all_words = defaultdict(Counter)
    start_words = Counter()

    for line_no, line in enumerate(io.open(corpus, 'r', encoding='utf-8')):
        if line_no % 100000 == 0:
            logging.info('Processing {0} sentences.'.format(line_no))

        tokens = tokenizer(line.strip(), separator)

        # don't process all uppercase, titlecase or lowercase sentences
        score = upper_score(tokens, separator)
        if score == 0 or score == 1.0:
            continue

        for tok in tokens:
            if not tok[0].isalpha() or separator in tok:
                continue
            all_words[tok.lower()][tok] += 1

        sent_start = 0
        if separator in tokens[0]:
            for i, tok in enumerate(tokens):
                if not separator in tok and tok[0].isupper():
                    sent_start = i
                    break

        if tokens[sent_start][0].isupper():
            start_words[tokens[sent_start].lower()] += 1

        if line_no >= max_sents:
            break

    with io.open(model, 'w', encoding='utf-8') as out:
        for word, count in start_words.most_common():
            if word == all_words[word].most_common(1)[0][0]:
                out.write('{0}\t{1}\n'.format(word, count))


if __name__ == '__main__':
    fire.Fire(main)
