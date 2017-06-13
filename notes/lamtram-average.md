
# Lamtram Averaged Models

Models ensemble generally improves the translation quality but reduces the speed and requires bigger resources. Here, we can use the alternative method by weight averaging, where the produced single model is element-wise average of the several identic models' parameters.

The original models used in this experiment are trained with Adam optimizer with learning rate `0.001` after 1 epoch and continued with SGD with learning rate `0.05`.

## Test Result (10,000 sentences)

Models | Dynet Mem | Time (User) | BLEU | BLEU (Lowercase)
--- | --- | -- | -- | --
Epoch 1 | 1000MB | 32m26.404s | 52.27 | 52.50
Epoch 2 | 1000MB | 31m54.348s | 52.35 | 52.56
Epoch 3 | 1000MB | 30m59.988s | 52.77 | 53.00
Ensemble | 4000MB | 95m21.748s | 53.07 | 53.29
Average | 1000MB | 31m36.572s | 52.92 | 53.14


## Commands

### Ensemble (Built-in)

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
xyz@0:~/workdir/nmt-pos$ python lamtram-average.py \
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

