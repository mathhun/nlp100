#!/usr/bin/env python

"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""

import re
import sys

def take_sentence(line):
    m = re.match('(.*?[.;:\?!]) ([A-Z].*)', line)

    if m:
        sentence = m.group(1)
        rest = m.group(2)

        return [sentence, rest]
    else:
        return [None, line]

def main():
    lines = open(sys.argv[1]).readlines()
    lines = [line.rstrip('\n') for line in lines]
    lines = filter(lambda x: len(x) > 0 , lines)
    text = ' '.join([line.rstrip('\n') for line in lines])

    sentences = []
    while True:
        s, r = take_sentence(text)
        if s is None:
            sentences.append(r)
            break
        sentences.append(s)
        text = r

    for s in sentences:
        print(s)

if __name__ == '__main__':
    main()
