
## AMUN

    $ head data/valid.en | amun-4574e3b -c clf.amun.npz.amun.yml
    [Sun June 11 06:06:18 2017] (I) Options: allow-unk: false
    beam-size: 1
    cpu-threads: 0
    devices: [0]
    gpu-threads: 1
    log-info: true
    log-progress: true
    max-length: 500
    maxi-batch: 1
    mini-batch: 1
    n-best: false
    no-debpe: false
    normalize: true
    relative-paths: false
    return-alignment: false
    return-soft-alignment: false
    scorers:
      F0:
        path: clf.amun.npz
        type: Nematus
    show-weights: false
    softmax-filter:
      []
    source-vocab: vocab.en.yml
    target-vocab: vocab.labels.yml
    weights:
      F0: 1
    wipo: false

    [Sun June 11 06:06:18 2017] (I) Loading scorers...
    [Sun June 11 06:06:18 2017] (I) Loading model clf.amun.npz onto gpu 0
    [Sun June 11 06:06:19 2017] (I) Reading from stdin
    [Sun June 11 06:06:19 2017] (I) Setting CPU thread count to 0
    [Sun June 11 06:06:19 2017] (I) Setting GPU thread count to 1
    [Sun June 11 06:06:19 2017] (I) Total number of threads: 1
    [Sun June 11 06:06:19 2017] (I) Reading input
    terminate called after throwing an instance of 'thrust::system::system_error'
      what():  cudaFree in free: unspecified launch failure


## S2S

    $ head data/valid.en | s2s-4574e3b -c clf.s2s.npz.s2s.yml
    [2017-06-11 06:07:38] [config] allow-unk: false
    [2017-06-11 06:07:38] [config] beam-size: 1
    [2017-06-11 06:07:38] [config] devices:
    [2017-06-11 06:07:38] [config]   - 0
    [2017-06-11 06:07:38] [config] dim-emb: 128
    [2017-06-11 06:07:38] [config] dim-pos: 0
    [2017-06-11 06:07:38] [config] dim-rnn: 256
    [2017-06-11 06:07:38] [config] dim-vocabs:
    [2017-06-11 06:07:38] [config]   - 10000
    [2017-06-11 06:07:38] [config]   - 10
    [2017-06-11 06:07:38] [config] input:
    [2017-06-11 06:07:38] [config]   - stdin
    [2017-06-11 06:07:38] [config] layer-normalization: false
    [2017-06-11 06:07:38] [config] layers-dec: 1
    [2017-06-11 06:07:38] [config] layers-enc: 1
    [2017-06-11 06:07:38] [config] max-length: 1000
    [2017-06-11 06:07:38] [config] maxi-batch: 1
    [2017-06-11 06:07:38] [config] mini-batch: 1
    [2017-06-11 06:07:38] [config] models:
    [2017-06-11 06:07:38] [config]   - clf.s2s.npz
    [2017-06-11 06:07:38] [config] n-best: false
    [2017-06-11 06:07:38] [config] normalize: true
    [2017-06-11 06:07:38] [config] relative-paths: true
    [2017-06-11 06:07:38] [config] seed: 1337
    [2017-06-11 06:07:38] [config] skip: true
    [2017-06-11 06:07:38] [config] tied-embeddings: true
    [2017-06-11 06:07:38] [config] type: s2s
    [2017-06-11 06:07:38] [config] vocabs:
    [2017-06-11 06:07:38] [config]   - /home/beritagar/workdir/gareng/classification/vocab.en.yml
    [2017-06-11 06:07:38] [config]   - /home/beritagar/workdir/gareng/classification/vocab.labels.yml
    [2017-06-11 06:07:38] [config] workspace: 512
    [2017-06-11 06:07:38] [data] Loading vocabulary from /home/beritagar/workdir/gareng/classification/vocab.en.yml (max: 10000)
    [2017-06-11 06:07:39] [data] Loading vocabulary from /home/beritagar/workdir/gareng/classification/vocab.labels.yml (max: 0)
    [2017-06-11 06:07:39] [memory] Extending reserved space to 512 MB (device 0)
    [2017-06-11 06:07:39] Loading model from clf.s2s.npz
    [2017-06-11 06:07:39] [memory] Reserving space for 3407370 floats (12 MB, device 0)
    Best translation 0 : 1
    Best translation 1 : 3
    Best translation 2 : 0
    Best translation 3 : 0
    Best translation 4 : 0
    Best translation 5 : 4
    Best translation 6 : 3
    Best translation 7 : 3
    Best translation 8 : 4
    Best translation 9 : 4
    1
    3
    0
    0
    0
    4
    3
    3
    4
    4
    [2017-06-11 06:07:39] Total time:  0.114350s wall, 0.100000s user + 0.010000s system = 0.110000s CPU (96.2%)

