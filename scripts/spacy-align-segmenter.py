# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import io
import string
import fire
import spacy
from spacy.tokens import Span

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def convert_alignment(a):
    return tuple(
        map(lambda x: tuple(map(lambda y: int(y), x.split('-'))), a.split()))


def extract(f_start, f_end, e_start, e_end, alignment, e_aligned, f_aligned,
            srctext, trgtext, srclen, trglen):
    if f_end < 0:  # 0-based indexing.
        return {}
    # Check if alignement points are consistent.
    for e, f in alignment:
        if ((f_start <= f <= f_end) and (e < e_start or e > e_end)):
            return {}

    # Add phrase pairs (incl. additional unaligned f)
    phrases = set()
    fs = f_start
    while True:
        fe = f_end
        while True:
            # add phrase pair ([e_start, e_end], [fs, fe]) to set E
            # Need to +1 in range  to include the end-point.
            src_phrase = " ".join(srctext[i]
                                  for i in range(e_start, e_end + 1))
            trg_phrase = " ".join(trgtext[i] for i in range(fs, fe + 1))
            # Include more data for later ordering.
            phrases.add(((e_start, e_end + 1), (f_start, f_end + 1),
                         src_phrase, trg_phrase))
            fe += 1
            # if fe is in word alignment or out-of-bounds
            if fe in f_aligned or fe == trglen:
                break
        fs -= 1
        # if fs is in word alignment or out-of-bounds
        if fs in f_aligned or fs < 0:
            break
    return phrases


def phrase_extraction(srctext, trgtext, alignment):
    srctext = srctext.split()  # e
    trgtext = trgtext.split()  # f
    srclen = len(srctext)  # len(e)
    trglen = len(trgtext)  # len(f)
    alignment = convert_alignment(alignment)
    # Keeps an index of which source/target words that are aligned.
    e_aligned = [i for i, _ in alignment]
    f_aligned = [j for _, j in alignment]

    bp = set()  # set of phrase pairs BP
    # Index e_start from 0 to len(e) - 1
    for e_start in range(srclen):
        # Index e_end from e_start to len(e) - 1
        for e_end in range(e_start, srclen):
            # // find the minimally matching foreign phrase
            # (f start , f end ) = ( length(f), 0 )
            # f_start ∈ [0, len(f) - 1]; f_end ∈ [0, len(f) - 1]
            f_start, f_end = trglen - 1, -1  #  0-based indexing
            # for all (e,f) ∈ A do
            for e, f in alignment:
                if e_start <= e <= e_end:
                    f_start = min(f, f_start)
                    f_end = max(f, f_end)
            # add extract (f start , f end , e start , e end ) to set BP
            phrases = extract(f_start, f_end, e_start, e_end, alignment,
                              e_aligned, f_aligned, srctext, trgtext, srclen,
                              trglen)
            if phrases:
                bp.update(phrases)
    return bp


def detokenize(text):
    text = ' ' + text + ' '
    text = text.replace('￭ ￭', '')
    text = text.replace('￭ ', '')
    text = text.replace(' ￭', '')
    return text.strip()


def main(input,
         output,
         alignment,
         min_length=2,
         max_length=15,
         spacy_model='en_core_web_sm'):
    nlp = spacy.load(spacy_model)

    def text_processing(text):
        doc = nlp(detokenize(text.strip()))

        for ent in doc.ents:
            ent.merge(ent.root.tag_, ent.text, ent.label_)

        for np in doc.noun_chunks:
            while len(np) > 1 and np[0].dep_ not in ('advmod', 'amod',
                                                     'compound'):
                np = np[1:]
            np.merge(np.root.tag_, np.text, np.root.ent_type_)

        segments = set()
        for tok in doc:
            left = tok.left_edge.i
            right = tok.right_edge.i + 1
            segment = Span(doc, left, right)
            if segment.root.dep_.upper() != 'ROOT' and len(segment) > 1:
                segments.add(segment)

        for other in list(sorted(segments, key=len, reverse=True)):
            for this in list(sorted(segments, key=len)):
                if len(this) < len(
                        other) and this.text_with_ws in other.text_with_ws:
                    segments.remove(this)

        for segment in segments:
            try:
                segment.merge(segment.root.tag_, segment.text,
                              segment.root.ent_type_)
            except IndexError:
                pass

        return doc


    with io.open(output, 'w', encoding='utf-8') as out_f, \
         io.open(input, 'r', encoding='utf-8') as in_f, \
         io.open(alignment, 'r', encoding='utf-8') as al_f:
        for line_no, (sent, align) in enumerate(zip(in_f, al_f)):

            try:
                src, tgt = sent.strip().split(' ||| ')
                doc = text_processing(src.strip())
            except Exception as e:
                logging.error('Error: {0}'.format(e))
                continue

            for s_idxs, t_idxs, s_phrase, t_phrase in phrase_extraction(
                    src, tgt, align):
                s_phrase = detokenize(s_phrase)
                t_phrase = detokenize(t_phrase)

                if s_phrase in string.punctuation or s_phrase.isdigit():
                    continue

                for span in list(doc):
                    if (span.text_with_ws == s_phrase and
                        (min_length <= len(span.text.split()) <= max_length)):
                        out_f.write('{0} ||| {1}\n'.format(s_phrase, t_phrase))

            if line_no % 10000 == 0:
                logging.info('Processed {0} lines'.format(line_no))


if __name__ == '__main__':
    fire.Fire(main)
