#!/usr/bin/env python

"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

import nlp030
import sys

def main(path):
    parsed = nlp030.mecab(path)
    for sentence in parsed:
        for word in sentence:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                print(word['base'])

if __name__ == '__main__':
    main(sys.argv[1])
