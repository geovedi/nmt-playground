import io
import re
import json
import html
import fire
from segtok.segmenter import split_single

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def preprocess(text):
    text = html.unescape(text)
    sents = []
    for sent in text.split('\n'):
        sent = sent.strip()
        if not sent:
            continue
        sent = re.sub(r'^', ' ', sent)
        sent = re.sub(r'$', ' ', sent)
        sent = re.sub(r' +', ' ', sent)

        sent = re.sub('•', '-', sent)
        sent = re.sub(r'[«»“”„‟『』]', '"', sent)
        sent = re.sub(r'[`ʼ‘’‚‛‹›「」]', "'", sent)
        sent = re.sub("''", '"', sent)
        sent = re.sub('…', '...', sent)
        sent = re.sub(r'\\', '', sent)
        sent = re.sub(r'([—–]|--| - |\u00AD)', ' — ', sent)
        sent = re.sub(' / ', '/', sent)
        sent = re.sub(';', '; ', sent)
        sent = re.sub("' s ", "'s ", sent)
        sent = re.sub(r'(\.\.+)', r' \1 ', sent)

        # ID specific
        sent = re.sub('Rp\.', 'Rp', sent)
        sent = re.sub(r' (sdr|prof|dr[ags]?|Mrs?|Ms|PS|Bpk)\. ', r' \1 ', sent, flags=re.I)
        sent = re.sub(r'^ ([A-Z]|\d+)\. ', r'\1) ', sent)
        sent = re.sub(r' ([A-Z]|\d+)\. ', r' \1 ', sent)

        sent = re.sub(r' +', ' ', sent)
        sent = re.sub(r'^ ', '', sent)
        sent = re.sub(r' $', '', sent)
        sents.append(sent)
    return '\n'.join(sents)


def main(input, output):
    with io.open(output, 'w', buffering=1, encoding='utf-8') as out:
        for line_no, line in enumerate(io.open(input, 'r', encoding='utf-8')):
            data = json.loads(line)
            if not data['text']:
                continue
            text = preprocess(data['text'])
            for sent in split_single(text):
                if sent:
                    out.write('{0}\n'.format(sent))
            if line_no % 10000 == 0:
                logging.info('Processed {0} documents.'.format(line_no))


if __name__ == '__main__':
    fire.Fire(main)
