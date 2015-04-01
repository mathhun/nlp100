#!/usr/bin/env python

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import math
import matplotlib.pyplot as plt
import nlp036
import numpy as np
import sys

def main(path):
    freq = nlp036.freq(path)

    _, counts = zip(*sorted(freq.items(), key=lambda x: x[1], reverse=True))
    indexes = np.arange(len(counts)) + 1

    log_counts  = [math.log(c) for c in counts]
    log_indexes = [math.log(i) for i in indexes]

    plt.plot(log_indexes, log_counts)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1])
