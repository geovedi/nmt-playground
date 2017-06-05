#!/usr/bin/env python3
import os
import io
import uuid
import subprocess
import fire
from pyaml import yaml
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

import logging
logging.basicConfig(
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def main(workdir, base_config, valid_src, valid_tgt, max_evals=100):
    if not os.path.exists(workdir):
        os.makedirs(workdir)

    config = yaml.load(io.open(base_config, 'r', encoding='utf-8'))

    def translator(weights):
        exp_id = str(uuid.uuid1())
        logging.info('Start experiment: id: "{0}", weights: {1}'
                     .format(exp_id, weights))

        exp_config = '{0}/{1}.yml'.format(workdir, exp_id)
        config['weights'] = weights
        with io.open(exp_config, 'w', encoding='utf-8') as out:
            out.write(yaml.dump(config))

        exp_out = '{0}/{1}.out'.format(workdir, exp_id)
        with io.open(valid_src, 'r', encoding='utf-8') as infile, \
             io.open(exp_out, 'w', encoding='utf-8') as outfile:
            cmd = ['amun', '-c', exp_config]
            proc = subprocess.Popen(cmd, stdin=infile, stdout=outfile)
            proc.wait()

        with io.open(exp_out, 'r', encoding='utf-8') as infile:
            cmd = ['run-scorer', 'BLEU', 'case:1', valid_tgt]
            proc = subprocess.Popen(cmd, stdin=infile, stdout=subprocess.PIPE)
        proc_out, proc_err = proc.communicate()
        score = float(proc_out)

        logging.info('End experiment: id: {0}, score: {1}'
                     .format(exp_id, score))
        loss = 1.0 - score
        return {'loss': loss, 'status': STATUS_OK}

    def create_space(weights):
        space = {}
        for key in weights.keys():
            space[key] = hp.uniform(key, 0, 1)
        return space

    trials = Trials()
    best = fmin(
        translator,
        space=create_space(config['weights']),
        algo=tpe.suggest,
        max_evals=max_evals,
        trials=trials)

    logging.info('Best: {0}'.format(best))


if __name__ == '__main__':
    fire.Fire(main)

