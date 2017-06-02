import io
import fire
import numpy as np

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def main(source_file, target_file, s2t_file, t2s_file, output_file, min_score=0.5):
    s2t = np.loadtxt(s2t_file)
    t2s = np.loadtxt(t2s_file)
    source = io.open(source_file, 'r', encoding='utf-8').read().strip().split('\n')
    target = io.open(target_file, 'r', encoding='utf-8').read().strip().split('\n')

    assert len(source) == len(target) == s2t.shape[0] == t2s.shape[0], 'mismatch sentences length'

    with io.open(output_file, 'w', encoding='utf-8') as out:
        for i, (src, tgt) in enumerate(zip(source, target)):
            s2t_score, t2s_score = s2t[i], t2s[i]
            if min([s2t_score, t2s_score]) > min_score:
                out.write('{src} ||| {tgt}\n'.format(src=src, tgt=tgt))
            if i % 1000 == 0:
                logging.info('Processed {0} sentences'.format(i))
        logging.info('Processed {0} sentences'.format(i))


if __name__ == '__main__':
    fire.Fire(main)

