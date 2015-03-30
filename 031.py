#!/usr/bin/env python

"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

import nlp030
import sys

def main(path):
    parsed = nlp030.mecab(path)
    for sentence in parsed:
        for word in sentence:
            if word['pos'] == '動詞':
                print(word['surface'])

if __name__ == '__main__':
    main(sys.argv[1])

