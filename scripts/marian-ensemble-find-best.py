#!/usr/bin/env python3
import os
import io
import uuid
import subprocess
import fire
import libamunmt as nmt
from pyaml import yaml
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

def main(workdir, base_config, valid_src, valid_tgt, max_evals=100):
    if not os.path.exists(workdir):
        os.makedirs(workdir)

    config = yaml.load(io.open(base_config, 'r', encoding='utf-8'))

    def translator(weights):
        exp_id = str(uuid.uuid1())
        print('Start experiment: id: "{0}", weights: {1}'
              .format(exp_id, weights))

        exp_config = '{0}/{1}.yml'.format(workdir, exp_id)
        config['weights'] = weights
        with io.open(exp_config, 'w', encoding='utf-8') as out:
            out.write(yaml.dump(config))
        nmt.init('-c {0}'.format(exp_config))

        exp_out = '{0}/{1}.out'.format(workdir, exp_id)
        with io.open(exp_out, 'w', encoding='utf-8') as out:
            for line in io.open(valid_src, 'r', encoding='utf-8'):
                text = line.strip()
                if text:
                    trans = nmt.translate([text])[0]
                else:
                    trans = ''
                out.write('{0}\n'.format(trans))

        with io.open(exp_out, 'r', encoding='utf-8') as infile:
            cmd = ['run-scorer', 'BLEU', 'case:1', valid_tgt]
            proc = subprocess.Popen(cmd, stdin=infile, stdout=subprocess.PIPE)
        proc_out, proc_err = proc.communicate()
        score = float(proc_out)

        print('End experiment: id: {0}, score: {1}'
              .format(exp_id, score))
        loss = 1.0 - score
        return {'loss': loss, 'status': STATUS_OK}

    def create_space(weights):
        space = {}
        for key in weights.keys():
            space[key] = hp.uniform(key, -1, 1)
        return space

    trials = Trials()
    best = fmin(
        translator,
        space=create_space(config['weights']),
        algo=tpe.suggest,
        max_evals=max_evals,
        trials=trials)

    print('Best: {0}'.format(best))


if __name__ == '__main__':
    fire.Fire(main)

