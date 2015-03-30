#!/usr/bin/env python

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

import nlp030
import sys

def main(path):
    parsed = nlp030.mecab(path)
    for sentence in parsed:
        for word in sentence:
            if word['pos'] == '動詞':
                print(word['base'])

if __name__ == '__main__':
    main(sys.argv[1])

