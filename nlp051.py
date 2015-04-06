#!/usr/bin/env python

"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""

import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.rstrip('\n')
            ws = line.split(' ')
            for w in ws:
                print(w)
            print('')

if __name__ == '__main__':
    main()
