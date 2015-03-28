#!/usr/bin/env python

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re
import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            m = re.search('<ref>(.*?)</ref>', line)
            if m:
                sys.stdout.write(m.group(1) + '\n')

if __name__ == '__main__':
    main()
