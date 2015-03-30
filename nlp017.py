#!/usr/bin/env python

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

import sys

"""
awk '{print $1}' data/hightemp.txt | sort -u
"""
def main():
    lines = open(sys.argv[1]).readlines()
    cols1 = [cols[0] for cols in [line.split() for line in lines]]
    counts = {}
    for col1 in cols1:
        counts.setdefault(col1, 0)
        counts[col1] += 1

    sorted_cols = sorted(counts.items(), key=lambda x: x[1])
    for k, v in sorted_cols:
        print(k)

if __name__ == '__main__':
    main()
