#!/usr/bin/env python

"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import nlp030
import sys

def main(path):
    parsed = nlp030.mecab(path)
    nouns_list = []
    for sentence in parsed:
        i = 0
        l = len(sentence)
        while i < l:
            nouns = []
            while sentence[i]['pos'] == '名詞':
                nouns.append(sentence[i]['surface'])
                i += 1
                if i >= l: break
            if len(nouns) > 1:
                nouns_list.append(''.join(nouns))
            i += 1
    return nouns_list

if __name__ == '__main__':
    print(main(sys.argv[1]))
