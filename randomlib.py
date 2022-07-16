import random
import string
import os

def generate_big_random_bin_file(filename,size):
    """
    generate big binary file with the specified size in bytes
    :param filename: the filename
    :param size: the size in bytes
    :return:void
    """
    with open('%s'%filename, 'wb') as fout:
        fout.write(os.urandom(size)) #1
    pass

def generate_big_random_letters(filename,size):
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    chars = ''.join([random.choice(string.letters) for i in range(size)]) #1

    with open(filename, 'w') as f:
        f.write(chars)
    pass

def generate_big_sparse_file(filename,size):
    f = open(filename, "wb")
    f.seek(size - 1)
    f.write("\1")
    f.close()
    pass

def generate_big_random_sentences(filename,linecount):
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")

    all = [nouns, verbs, adj, adv]

    with open(filename,'w') as f:
        for i in range(linecount):
            f.writelines([' '.join([random.choice(i) for i in all]),'\n'])
    pass

def gen_32_rand_bits():
    rnd_32bits = f'{random.getrandbits(32):=032b}'
    return rnd_32bits

#generate_big_random_bin_file("test.bin", 1024*1024)
generate_big_random_sentences("test.bin", 1000000)

import zlib, sys

filename_in = "test.bin"
filename_out = "test.bin.compressed"

with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 1000033
    print(f"Comprssd size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 1024
    fout.write(compressed_data)
