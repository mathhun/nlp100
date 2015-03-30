#!/usr/bin/env python

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys
from optparse import OptionParser

"""
head -n
"""
def main():
    parser = OptionParser()
    parser.add_option("-n", None, type="int", dest="nlines", help="count")
    (options, args) = parser.parse_args()
    f = open(args[0])
    for i in range(options.nlines):
        sys.stdout.write(f.readline())

if __name__ == '__main__':
    main()
