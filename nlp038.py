#!/usr/bin/env python

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import matplotlib.pyplot as plt
import nlp036
import numpy as np
import sys

def main(path):
    freq = nlp036.freq(path)

    hist = {}
    for k, v in freq.items():
        v = (v // 100) * 100
        hist.setdefault(v, 0)
        hist[v] += 1

    freqs, kinds = zip(*sorted(hist.items(), key=lambda x: x[0]))
    print(freqs)
    print(kinds)

    indexes = np.arange(len(freqs))
    width = 0.7
    plt.bar(indexes, freqs, width)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1])

