import io
import re
import string
import argparse
from collections import Counter


import logging

logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


UNWANTED = string.punctuation + ' —\n'

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



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', required=True, help='Count files')
    parser.add_argument('-o', '--output', required=True, help='Output')
    parser.add_argument('-n', '--min-count', default=2, help='Min count')
    args = parser.parse_args()

    counter = Counter()

    for fname in args.files:
        logging.info('Working on {0}'.format(fname))
        for line_no, line in enumerate(io.open(fname, 'r', encoding='utf-8')):
            count, phrase = line.strip().split('\t')
            phrase = cleanup(phrase)
            counter[phrase] += int(count)
            if line_no % 10000 == 0:
                logging.info('Processed {0} lines'.format(line_no))
        logging.info('Processed {0} lines'.format(line_no))

    with io.open(args.output, 'w', encoding='utf-8') as out:
        for phrase, count in counter.most_common():
            if count >= min-count:
                out.write('{0}\t{1}\n'.format(count, phrase))
            else:
                break


if __name__ == '__main__':
    main()

