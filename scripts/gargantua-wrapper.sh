#!/bin/bash
BASEDIR=/path/to/gargantua
SOURCE_DIR=${BASEDIR}/sources
TARGET_DIR=${BASEDIR}/targets
FILELIST=$1
OUTPUT_DIR=$2
SENT_TOKENIZER=sentences-linux64
WORD_TOKENIZER=tokenize.sed

(cd ${BASEDIR} && ./clean.sh && ./prepare-filesystem.sh)

cat ${FILELIST} | while read fname; do 
    echo ${fname};
    cat ${SOURCE_DIR}/${fname} | ${SENT_TOKENIZER} | grep -v "^$" \
        > ${BASEDIR}/corpus_to_align/source_language_corpus_untokenized/${fname};
    cat ${SOURCE_DIR}/${fname} | ${SENT_TOKENIZER} | grep -v "^$" \
        > ${BASEDIR}/corpus_to_align/target_language_corpus_untokenized/${fname};
    cat ${BASEDIR}/corpus_to_align/source_language_corpus_untokenized/${fname} | \
        ${WORD_TOKENIZER} | perl -CSA -ne 'print lc' \
        > ${BASEDIR}/corpus_to_align/source_language_corpus_tokenized/${fname};
    cat ${BASEDIR}/corpus_to_align/target_language_corpus_untokenized/${fname} | \
        ${WORD_TOKENIZER} | perl -CSA -ne 'print lc' \
        > ${BASEDIR}/corpus_to_align/target_language_corpus_tokenized/${fname};
done

(cd ${BASEDIR} && ./prepare-data.sh)

(cd ${BASEDIR}/workdir && ./sentence-aligner)

mv ${BASEDIR}/workdir/output_data_aligned ${OUTPUT_DIR}
