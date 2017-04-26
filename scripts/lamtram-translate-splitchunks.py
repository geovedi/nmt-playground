# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io
import regex as re
import subprocess
import plac


class Segmenter(object):
    SPLIT_AFTER = (', ', ') ', '} ', '] ', '| ', ' -- ', ': ', '; ', '. ', '? ', '! ', '" ', )
    SPLIT_BEFORE = (' (', ' {', ' [', ' |', ' http://', ' https://', ' ftp://', )

    def __init__(self, code_fname, separator='￭'):
        self.codes = [tuple(item.split()) for item in io.open(code_fname, encoding='utf-8')]
        self.codes = dict([(code, i) for (i, code) in reversed(list(enumerate(self.codes)))])
        self.separator = separator
        self.cache = {}

    def segment(self, sentence):
        output = []
        for word in self.tokenize(sentence):
            if word in ['|||', '<unk>'] or self.separator in word:
                output.append(word)
            else:
                new_word = self.encode(word, self.codes)
                for item in new_word[:-1]:
                    output.append(item + self.separator)
                output.append(new_word[-1])
        return ' '.join(output)

    def tokenize(self, text):
        text = re.sub(r'^', ' ', text)
        text = re.sub(r'$', ' ', text)
        text = re.sub('•', '-', text)
        text = re.sub(r'[«»“”„‟『』]', '"', text)
        text = re.sub(r'[`ʼ‘’‚‛‹›「」]', "'", text)
        text = re.sub("''", '"', text)
        text = re.sub('…', '...', text)
        text = re.sub(r'([—–]| - )', ' -- ', text)
        text = re.sub(' / ', '/', text)
        text = re.sub(';', '; ', text)
        text = re.sub("' s", "'s ", text)
        text = re.sub(r'(\.\.+)', r' \1 ', text)
        text = re.sub(r'([\p{L}\p{N}])([\p{P}\p{S}]+) ', r'\1 {}\2 '.format(self.separator), text)
        text = re.sub(r' ([\p{P}\p{S}]+)([\p{L}\p{N}])', r' \1{} \2'.format(self.separator), text)
        text = re.sub(r'([\p{L}\p{N}])([\p{P}\p{S}]+)([\p{L}\p{N}])', r'\1 {}\2{} \3'.format(self.separator, self.separator), text)
        text = re.sub(r' ([\p{N}]+)([\p{L}])', r' \1 \2', text)
        text = re.sub(r" {}'{} ([sSmMdD]|ll|re|ve|LL|RE|VE) ".format(self.separator, self.separator), r" {}'\1 ".format(self.separator), text)
        text = re.sub(r"([Nn]) {}'{} ([Tt])".format(self.separator, self.separator), r" {}\1'\2 ".format(self.separator), text)
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'^ ', '', text)
        text = re.sub(r' $', '', text)
        return text.split()

    def detokenize(self, text):
        text = re.sub(r'^', ' ', text)
        text = re.sub(r'$', ' ', text)
        text = re.sub(r" {}'([sSmMdD]|ll|re|ve|LL|RE|VE) ".format(self.separator), r"'\1 ", text)
        text = re.sub(r" {}([Nn])'([Tt]) ".format(self.separator), r"\1'\2 ", text)
        text = re.sub('{} {}'.format(self.separator, self.separator), '', text)
        text = re.sub('{} '.format(self.separator), '', text)
        text = re.sub(' {}'.format(self.separator), '', text)
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'^ ', '', text)
        text = re.sub(r' $', '', text)
        return text

    def get_pairs(self, word):
        pairs = set()
        prev_char = word[0]
        for char in word[1:]:
            pairs.add((prev_char, char))
            prev_char = char
        return pairs

    def encode(self, orig, codes):
        if orig in self.cache:
            return self.cache[orig]

        word = tuple(orig) + ('</w>', )
        pairs = self.get_pairs(word)

        while True:
            bigram = min(pairs, key=lambda pair: codes.get(pair, float('inf')))
            if bigram not in codes:
                break
            first, second = bigram
            new_word = []
            i = 0
            while i < len(word):
                try:
                    j = word.index(first, i)
                    new_word.extend(word[i:j])
                    i = j
                except:
                    new_word.extend(word[i:])
                    break

                if word[i] == first and i < len(word) - 1 and word[i + 1] == second:
                    new_word.append(first + second)
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_word = tuple(new_word)
            word = new_word
            if len(word) == 1:
                break
            else:
                pairs = self.get_pairs(word)

        # don't print end-of-word symbols
        if word[-1] == '</w>':
            word = word[:-1]
        elif word[-1].endswith('</w>'):
            word = word[:-1] + (word[-1].replace('</w>', ''), )

        self.cache[orig] = word
        return word

    def punct_split(self, word):
        word = re.sub(r'^([\p{P}]+)([\p{L}\p{N}]+)', r'\1{} \2'.format(self.separator), word)
        word = re.sub(r'([\p{L}\p{N}]+)([\p{P}]+)$', r'\1 {}\2'.format(self.separator), word)
        return word

    def split(self, sent, max_length=50):
        sent = sent.strip()
        sent = ' '.join(self.punct_split(word) for word in sent.split())
        for pat in self.SPLIT_AFTER:
            sent = sent.replace(pat, pat + '\n')
        for pat in self.SPLIT_BEFORE:
            sent = sent.replace(pat, '\n' + pat)
        sents = sent.split('\n')

        chunks, PREV_LEN = [], 0
        for i, chunk in enumerate(sents):
            chunk = self.segment(chunk.strip())
            CHUNK_LEN = len(chunk.split())
            if i > 0:
                if (PREV_LEN + CHUNK_LEN) < max_length:
                    chunks[-1] += ' ' + chunk
                    PREV_LEN = len(chunks[-1].strip().split())
                else:
                    chunks.append(chunk)
                    PREV_LEN = CHUNK_LEN
            else:
                chunks.append(chunk)
                PREV_LEN = CHUNK_LEN

        # if last chunks is too short, merged with the previous one
        if len(chunks) > 2:
            if len(chunks[-1].split()) < 4:
                chunks[-2] += ' ' + chunks[-1]
                chunks.remove(chunks[-1])

        return chunks


def main(model, codes, input_fname, output_fname, detokenize=False, segment_length=20):
    segmenter = Segmenter(codes)
    lamtram_cmd = '''
        lamtram
            --dynet-mem 1000
            --models_in encatt={0}
            --operation gen
    '''.format(model).split()

    proc = subprocess.Popen(lamtram_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    with io.open(output_fname, 'w', buffering=1, encoding='utf-8') as out:
        for line in io.open(input_fname, 'r', encoding='utf-8'):
            translated = []
            for segment in segmenter.split(line, max_length=segment_length):
                segment = segment + '\n'
                proc.stdin.write(segment.encode('utf-8'))
                proc.stdin.flush()
                text = proc.stdout.readline().strip()
                if text:
                    text = text.decode('utf-8')
                    if detokenize:
                        text = segmenter.detokenize(text)
                    translated.append(text)
            translated = ' '.join(translated).strip()
            out.write('{0}\n'.format(translated))

    proc.terminate()


if __name__ == '__main__':
    plac.call(main)
