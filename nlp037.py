#!/usr/bin/env python

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import nlp036
import matplotlib.pyplot as plt
import numpy as np
import sys

def main(path):
    freq = nlp036.freq(path)
    freq10 = nlp036.sort_freq(freq)[0:10]
    labels, values = zip(*freq10)

    indexes = np.arange(len(labels))
    width = 1
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1])
