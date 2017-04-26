# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io
import fire
import numpy as np


def num2str(num, dtype):
    if dtype == np.float64:
        return '{0:.4f}'.format(num)
    elif dtype == np.int64:
        return '{0:n}'.format(num)
    return num


def read_files(fnames):
    in_files = [iter(io.open(f, 'r', encoding='utf-8')) for f in fnames]
    for lines in zip(*in_files):
        yield [line.strip() for line in lines]


def main(output_file, input_files, sep='|'):
    input_files = input_files.split(sep)
    num_files = len(input_files)

    with io.open(output_file, 'w', buffering=1, encoding='utf-8') as out:
        for lines in read_files(input_files):
            result = []
            for cols in zip(*map(lambda x: x.split(), lines)):
                if len(set(cols)) == 1:
                    result.append(cols[0])
                else:
                    f = io.BytesIO('\n'.join(cols).encode('utf-8'))
                    cols_arr = np.genfromtxt(f, dtype=None)
                    cols_weight = sum(cols_arr) / num_files
                    result.append(num2str(cols_weight, cols_arr.dtype))
            out.write('{0}\n'.format(' '.join(result)))


if __name__ == '__main__':
    fire.Fire(main)
