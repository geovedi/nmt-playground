import io
import fire

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def main(source_file, target_file, s2t_file, t2s_file, out_file, min_score=0.5):
    source = io.open(source_file, 'r', encoding='utf-8')
    target = io.open(target_file, 'r', encoding='utf-8')
    s2t = io.open(s2t_file, 'r', encoding='utf-8')
    t2s = io.open(t2s_file, 'r', encoding='utf-8')

    with io.open(out_file, 'w', encoding='utf-8') as out:
        for i, pair in enumerate(zip(source, target, s2t, t2s)):
            (src, tgt, s2t_score, t2s_score) = pair

            if min([float(s2t_score), float(t2s_score)]) > min_score:
                out.write('{src} ||| {tgt}\n'.format(src=src, tgt=tgt))

            if i % 1000 == 0:
                logging.info('Processed {0} sentences'.format(i))
        logging.info('Processed {0} sentences'.format(i))


if __name__ == '__main__':
    fire.Fire(main)
