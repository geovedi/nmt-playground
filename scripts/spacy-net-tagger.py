import io
import json
import fire
import spacy

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def main(input, output):
    nlp = spacy.load('en_core_web_sm')

    with io.open(output, 'w', encoding='utf-8') as out:
        for line_no, line in enumerate(io.open(input, 'r', buffering=1, encoding='utf-8')):
            text = line.strip()
            doc = nlp(text)
            for ent in doc.ents:
                ent.merge(ent.root.tag_, ent.text, ent.label_)
            entities = [(tok.idx, tok.idx + len(tok.text), tok.ent_type_) for tok in doc if tok.ent_type_ != '']
            data = (text, entities)
            out.write(json.dumps(data, ensure_ascii=False))
            out.write('\n')

            if line_no % 10000 == 0:
                logging.info('Processed {0} sentences.'.format(line_no))

        logging.info('Processed {0} sentences.'.format(line_no))


if __name__ == '__main__':
    fire.Fire(main)

