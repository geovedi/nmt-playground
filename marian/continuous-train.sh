#!/bin/bash

BINDIR=./bin.27ef488
DATADIR=./data
BASE=base.bpe
TRAIN=train.bpe
SRC=en
TGT=id
SRC2TGT=${SRC}2${TGT}
NUMPARTS=5
MAXSENTS=2000000

PARTS=$(seq -s ' ' -f %03g ${NUMPARTS} | xargs -n 1 | shuf)

for PART in ${PARTS}; do
    if [ -f model.${SRC2TGT}.npz.best-cross-entropy.npz ]; then
        ${BINDIR}/rescorer \
            --model model.${SRC2TGT}.npz.best-cross-entropy.npz \
            --train-sets ${DATADIR}/${BASE}.${PART}.${SRC} ${DATADIR}/${BASE}.${PART}.${TGT} \
            --vocabs vocab.en.json vocab.id.json \
            > ${DATADIR}/${BASE}.${PART}.scores
    fi

    paste-files.pl \
        ${DATADIR}/${BASE}.${PART}.scores \
        ${DATADIR}/${BASE}.${PART}.${SRC} \
        ${DATADIR}/${BASE}.${PART}.${TGT} | \
        sort -g | \
        head -n ${MAXSENTS} \
        > ${DATADIR}/${TRAIN}.${SRC2TGT}.pairs

    paste-files.pl \
        <(cut-corpus.pl 2 ${DATADIR}/${TRAIN}.${SRC2TGT}.pairs) \
        <(cut-corpus.pl 3 ${DATADIR}/${TRAIN}.${SRC2TGT}.pairs) \
        > ${DATADIR}/${TRAIN}.${SRC2TGT}

    fast_align \
        -d -o -v  \
        -i ${DATADIR}/${TRAIN}.${SRC2TGT} \
        > ${DATADIR}/${TRAIN}.${SRC2TGT}.fwd

    fast_align \
        -d -o -v -r \
        -i ${DATADIR}/${TRAIN}.${SRC2TGT} \
        > ${DATADIR}/${TRAIN}.${SRC2TGT}.rev

    atools \
        -i ${DATADIR}/${TRAIN}.${SRC2TGT}.fwd \
        -j ${DATADIR}/${TRAIN}.${SRC2TGT}.rev \
        -c grow-diag-final-and \
        > ${DATADIR}/${TRAIN}.${SRC2TGT}.align

    ${BINDIR}/marian \
        --config train.${SRC2TGT}.yml \
        --guided-alignment ${DATADIR}/${TRAIN}.${SRC2TGT}.align

done
