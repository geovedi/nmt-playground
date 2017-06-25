import io
import re
import fire

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

UNWANTED = re.compile('[^'
    '\u0000-\u007f\u0080-\u00ff\u0100-\u017F\u1E00-\u1EFF\u0180-\u024F'
    '\u2C60-\u2C7F\uA720-\uA7FF\uAB30-\uAB6F'
    '\u2014\u0024\u00a2-\u00a5\u0e3f\u20a0\u20a1\u20a3-\u20a5\u20ac'
    '\uffe1\uffe5\u20b9'
    ']', re.UNICODE)


def smart_open(filename, mode="rt", ftype="auto", encoding='utf-8', errors='replace'):
    if ftype == 'gzip' or ftype == 'gz' or (ftype == 'auto' and filename.endswith(".gz")):
        import gzip
        return gzip.open(filename, mode=mode, encoding=encoding, errors=errors)
    elif ftype == "bzip2" or ftype == "bz2" or (ftype == 'auto' and filename.endswith(".bz2")):
        import bz2
        return bz2.open(filename, mode=mode, encoding=encoding, errors=errors)
    else:
        return open(filename, mode=mode, encoding=encoding, errors=errors)


def main(input, output):
    with smart_open(output, 'wt') as out:
        for line_no, line in enumerate(smart_open(input, 'rt')):
            if UNWANTED.search(line):
                continue
            out.write(line)
            if line_no % 10000 == 0:
                logging.info('Processed {0} sentences.'.format(line_no))


if __name__ == '__main__':
    fire.Fire(main)
