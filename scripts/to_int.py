import io
import fire


UNK = '<unk>'

def read_vocab(fname):
    vocab = {}
    for line in io.open(fname, 'r', encoding='utf-8'):
        w, i = line.strip().split('\t', 1)
        vocab[w] = i # keep as string
    return vocab


def main(input, output, vocab):
    v = read_vocab(vocab)
    uv = v.get(UNK)

    with io.open(output, 'w', encoding='utf-8') as out:
        for line in io.open(input, 'r', encoding='utf-8'):
            tokens = line.strip().split()
            ints = [v.get(w, uv) for w in tokens]
            out.write('{0}\n'.format(' '.join(ints)))


if __name__ == '__main__':
    fire.Fire(main)

