#!/usr/bin/env python

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

from collections import Counter
import matplotlib.pyplot as plt
import nlp030
import nlp036
import math
import numpy as np
import sys

def main(path):
    freq = nlp036.freq(path)
    freq10 = nlp036.sort_freq(freq)
    words, frequencies = zip(*freq10)

    fs = []
    for x in frequencies:
        fs.append(math.log(x))

    print(words[0:10])
    print(frequencies[0:10])
    print(fs[0:10])

    plt.hist(fs, bins=20)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1])

