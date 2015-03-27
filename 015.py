#!/usr/bin/env python
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys
from optparse import OptionParser

"""
tail -n
"""
def main():
    parser = OptionParser()
    parser.add_option("-n", None, type="int", dest="nlines", help="count")
    (options, args) = parser.parse_args()
    lines = open(args[0]).readlines()
    for line in lines[len(lines) - options.nlines :]:
        sys.stdout.write(line)

if __name__ == '__main__':
    main()
