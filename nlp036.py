#!/usr/bin/env python

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import nlp030
import sys

import pprint
pp = pprint.PrettyPrinter()

def freq(path):
    parsed = nlp030.mecab(path)
    dic = {}
    for sentence in parsed:
        for word in sentence:
            dic.setdefault(word['base'], 0)
            dic[word['base']] += 1
    return dic

def sort_freq(dic):
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    f = freq(sys.argv[1])
    s = sort_freq(f)
    s = s[0:10]
    print(s)
