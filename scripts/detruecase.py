#!/usr/bin/env python3
import sys
import re
import string

PUNCTUATION = string.punctuation + '—'


def preprocess(text):
    return text


def postprocess(text):
    text = re.sub('(^| )- ', r'\1— ', text)
    text = re.sub(r'([\$£]|Rp) (\d+)', r'\1\2', text)
    text = re.sub(r'(US) (\/|\$|£)\s?(\d+)', r'\1$\3', text) # bug in earlier model
    text = re.sub(r'^>\s?"\s?', '> "', text)
    text = re.sub(r'^(\d+) \'- ', r"\1' — ", text)
    text = re.sub(r'\s?([\/]+)\s?', r'\1', text)
    return text


def ispunct(char, separator='￭'):
    if char in PUNCTUATION:
        return True
    return False


def detokenize(text, separator='￭'):
    text = text.replace('{sep} {sep}'.format(sep=separator), '')
    text = text.replace('{sep} '.format(sep=separator), '')
    text = text.replace(' {sep}'.format(sep=separator), '')
    return text


def tokenize(text, separator='￭'):
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


def detruecase(text, separator='￭'):
    tokens = tokenize(text, separator=separator)
    if not tokens:
        return text

    sent_start = 0
    if ispunct(tokens[0][0], separator=separator):
        for i, tok in enumerate(tokens):
            if not ispunct(tok[0], separator=separator):
                sent_start = i
                break

    if tokens[sent_start][0].isdigit():
        return text
    elif tokens[sent_start][0].isupper():
        return text

    tokens[sent_start] = tokens[sent_start].title()
    return detokenize(' '.join(tokens), separator=separator)


if __name__ == '__main__':
    separator='￭'

    for line in sys.stdin:
        text = line.strip()
        if text is None:
            print('')

        text = preprocess(text)

        if separator in text:
            text = detruecase(detokenize(text, separator=separator), separator=separator)
        else:
            text = detruecase(text, separator=separator)

        text = postprocess(text)

        print(text)


