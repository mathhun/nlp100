#!/usr/bin/env python

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import re
import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            if re.search('\[\[Category:.*?\]\]', line):
                sys.stdout.write(line)

if __name__ == '__main__':
    main()
