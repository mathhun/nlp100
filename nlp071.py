#!/usr/bin/env python

"""
71. ストップワード

英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単
語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さら
に，その関数に対するテストを記述せよ．
"""

import sys

class StopList():
    def __init__(self):
        self.stoplist = []

    def load(self, path):
        self.stoplist = [line.strip() for line in open(path).readlines()]

    def set_stoplist(self, stoplist):
        self.stoplist = stoplist

    def in_stoplist(self, word):
        if word in self.stoplist:
            return True
        else:
            return False

def main():
    sl = StopList()
    sl.load("./data/stoplist")
    w = sys.argv[1]
    if sl.in_stoplist(w):
        print("In stoplist: '{0}'".format(w))
    else:
        print("Not in stoplist: '{0}'".format(w))

if __name__ == '__main__':
    main()
