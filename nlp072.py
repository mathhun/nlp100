#!/usr/bin/env python

"""
72. 素性抽出

極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビュー
からストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであ
ろう．
"""

from collections import Counter
from stemming.porter2 import stem
from nlp071 import StopList

class WordList():
    def __init__(self, positive=True):
        self.positive = positive
        self.lines = []
        self.words = []
        self.stoplist = None
        self.counts = {}
        self.feature = None

    def loadfile(self, path):
        self.lines = open(path, encoding="latin_1").readlines()
        self.words = [ word.strip() for line in self.lines for word in line.split(" ") ]

    def in_stoplist(self, word):
        if word == '':
            return True
        return self.stoplist.in_stoplist(word)
        
    def filter_stopwords(self):
        self.stoplist = StopList()
        self.stoplist.load("./data/stoplist")
        self.words = [ word for word in self.words if not self.in_stoplist(word) ]

    def stemall(self):
        self.words = [ stem(word) for word in self.words ]

    def count(self):
        self.counts = Counter(self.words)

    def delete(self, words):
        for w in words:
            del self.counts[w]

    def most_common(self, thres=100):
        return self.counts.most_common(thres)

def setup():
    pos = WordList()
    pos.loadfile("data/rt-polaritydata/rt-polarity.pos")
    pos.filter_stopwords()
    pos.stemall()
    pos.count()

    neg = WordList()
    neg.loadfile("data/rt-polaritydata/rt-polarity.neg")
    neg.filter_stopwords()
    neg.stemall()
    neg.count()

    #print("pos count")
    #print(len(pos.words))
    #print("neg count")
    #print(len(neg.words))

    #pos.delete(neg.words)
    #neg.delete(pos.words)

    #print("---pos---")
    #print(pos.most_common(100))
    #print("---neg---")
    #print(neg.most_common(100))
    #print("\n")

    return pos, neg

if __name__ == '__main__':
    setup()
