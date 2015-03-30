#!/usr/bin/env python

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re
import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            m = re.search('\[\[Category:(.*?)\]\]', line)
            if m:
                sys.stdout.write(m.group(1) + '\n')

if __name__ == '__main__':
    main()
