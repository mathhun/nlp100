#!/usr/bin/env python

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys

"""
cut -f1 data/hightemp.txt | sort | uniq -c | sort -r
"""
def main():
    lines = open(sys.argv[1]).readlines()
    cols1 = [cols[0] for cols in [line.split() for line in lines]]
    counts = {}
    for col1 in cols1:
        counts.setdefault(col1, 0)
        counts[col1] += 1

    sorted_list = sorted(counts.items(), key=lambda x: -x[1])
    for k, v in sorted_list:
        print("{0:4d} {1}".format(v, k))

if __name__ == '__main__':
    main()

