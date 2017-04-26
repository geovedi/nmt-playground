
# Lamtram Averaged Models

Averaged model built from the several trained models from **the same training parameters**.

## Test Result (10,000 sentences)

Models | Dynet Mem | Time (User) | BLEU | BLEU (Lowercase)
--- | --- | -- | -- | --
Epoch 1 | 1000MB | 32m26.404s | 52.35 | 52.56
Epoch 2 | 1000MB | 31m54.348s | 52.27 | 52.50
Epoch 3 | 1000MB | 30m59.988s | 52.77 | 53.00
Ensemble (default) | 4000MB | 95m21.748s | 53.07 | 53.29
Ensemble (post-processing: avg) | 1000MB | 31m36.572s | 52.92 | 53.14


## Commands

### Default

```bash

xyz@0:~/workdir/nmt-pos$ time lamtram-cpu \
    --dynet-mem 4000 \
    --operation gen \
    --minibatch_size 4096 \
    --src_in data/dev/dev.en \
    --models_in "encatt=bpe10k.en2id.lstm128x4.model.e1|encatt=bpe10k.en2id.lstm128x4.model.e2|encatt=bpe10k.en2id.lstm128x4.model.e3" \
    --ensemble_op sum \
    > data/dev/dev.en.id.ens.default
```

### Averaging

```bash
xyz@0:~/workdir/nmt-pos$ python ensemble.py \
    --output-file bpe10k.en2id.lstm128x4.model.ens.avg \
    --input-files "bpe10k.en2id.lstm128x4.model.e1|bpe10k.en2id.lstm128x4.model.e2|bpe10k.en2id.lstm128x4.model.e3"

xyz@0:~/workdir/nmt-pos$ time lamtram-cpu \
    --dynet-mem 1000 \
    --operation gen \
    --minibatch_size 4096 \
    --src_in data/dev/dev.en \
    --models_in encatt=bpe10k.en2id.lstm128x4.model.ens.avg \
    > data/dev/dev.en.id.ens.avg
```

