# -*- coding: utf-8 -*-

import io
import string
import re
import fire
import spacy
from collections import Counter
from spacy.tokens import Span
from joblib import Parallel, delayed

import logging

logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def detokenize(text):
    text = ' ' + text + ' '
    text = text.replace('￭ ￭', '')
    text = text.replace('￭ ', '')
    text = text.replace(' ￭', '')
    return text.strip()


UNWANTED = string.punctuation + ' \n'
#PAREN_OPENED = '<({['
#PAREN_CLOSED = '>)}]'
#PAREN_OPENED_REGEXP = re.compile(r'[\<\[\{\(]')
#PAREN_CLOSED_REGEXP = re.compile(r'[\>\]\}\)]')
#PAREN_PAIRS = {
#    '<': '>', '(': ')', '{': '}', '[': ']',
#    '>': '<', ')': '(', '}': '{', ']': '['
#}

# fix spacy parsing result only
PAREN_OPENED = ['(', ' "']
PAREN_CLOSED = [')', '" ']
PAREN_OPENED_REGEXP = re.compile(r'([\(]| ")')
PAREN_CLOSED_REGEXP = re.compile(r'([\)]|" )')
PAREN_PAIRS = {'(': ')', ')': '(', ' "': '" ', '" ': ' "'}


def find_missing_pairs(text):
    opened_count = Counter(PAREN_OPENED_REGEXP.findall(text))
    closed_count = Counter(PAREN_CLOSED_REGEXP.findall(text))
    result = {}

    for this_char, this_count in opened_count.items():
        pair_char = PAREN_PAIRS[this_char]
        pair_count = closed_count[pair_char]
        if this_count > pair_count:
            result[pair_char] = this_count - pair_count
        elif this_count < pair_count:
            result[this_char] = pair_count - this_count

    for this_char, this_count in closed_count.items():
        pair_char = PAREN_PAIRS[this_char]
        pair_count = opened_count[pair_char]
        if this_count > pair_count:
            result[pair_char] = this_count - pair_count
        elif this_count < pair_count:
            result[this_char] = pair_count - this_count

    return result


def cleanup(text):
    text = text.strip(UNWANTED)
    for char, count in find_missing_pairs(text).items():
        if char in PAREN_OPENED:
            text = ''.join([char.strip()] * count) + text
        elif char in PAREN_CLOSED:
            text = text + ''.join([char.strip()] * count)
    return text


def text_processing(model, text, min_length, max_length):
    nlp = spacy.load(model)
    doc = nlp(text)
    mini_counter = Counter()

    for ent in doc.ents:
        ent.merge(ent.root.tag_, ent.text, ent.label_)
        if min_length <= len(ent) <= max_length:
            phrase = cleanup(ent.text)
            if phrase and not '\n' in phrase:
                mini_counter[phrase] += 1

    for np in doc.noun_chunks:
        while len(np) > 1 and np[0].dep_ not in ('advmod', 'amod', 'compound'):
            np = np[1:]
        np.merge(np.root.tag_, np.text, np.root.ent_type_)
        if min_length <= len(np) <= max_length:
            phrase = cleanup(np.text)
            if phrase and not '\n' in phrase:
                mini_counter[phrase] += 1

    for sent in doc.sents:
        for tok in sent:
            left = tok.left_edge.i
            right = tok.right_edge.i + 1
            segment = Span(doc, left, right)
            if (segment.root.dep_.upper() != 'ROOT' and
                    min_length <= len(segment) <= max_length):
                phrase = cleanup(segment.text)
                if phrase and not '\n' in phrase:
                    mini_counter[phrase] += 1

    return mini_counter


def produce(input, sentence_limit):
    mini_buckets = []

    for line_no, line in enumerate(io.open(input, 'r', encoding='utf-8')):
        line_no += 1
        try:
            if ' ||| ' in line:
                src, tgt = line.strip().split(' ||| ')
                text = src
            else:
                text = line
        except:
            continue

        text = detokenize(text)

        # hack
        if text[-1] != ".":
            text = text + '.'

        mini_buckets.append(text)

        if line_no % 1000 == 0:
            yield '\n'.join(mini_buckets)
            mini_buckets = []

        if line_no >= sentence_limit:
            break

    # leftovers
    if mini_buckets:
        yield '\n'.join(mini_buckets)


def main(input,
         output,
         model='en_core_web_sm',
         sentence_limit=2000000,
         n_jobs=4,
         min_length=2,
         max_length=10):
    results = Parallel(
        n_jobs=n_jobs, verbose=5)(
            delayed(text_processing)(model, text, min_length, max_length)
            for text in produce(input, sentence_limit))

    counter = Counter()
    for result in results:
        counter.update(result)

    logging.info('writing counts to {0}'.format(output))
    with io.open(output, 'w', encoding='utf-8') as out:
        for phrase, count in counter.items():
            out.write('{0}\t{1}\n'.format(count, phrase))


if __name__ == '__main__':
    fire.Fire(main)
