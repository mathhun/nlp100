#!/usr/bin/env python

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            m = re.search('(=+) +(.*?) +(=+)', line)
            if m:
                print("{0} {1}".format(len(m.group(1))-1, m.group(2)))

if __name__ == '__main__':
    main()
