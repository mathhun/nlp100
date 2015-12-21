#!/usr/bin/env python

"""
74. 予測

73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例な
ら"-1"）と，その予測確率を計算するプログラムを実装せよ．
"""

from stemming.porter2 import stem
from nlp071 import StopList
from nlp073 import Model

class BagOfWords():
    def __init__(self):
        self.lines = []
        self.bow = []

        self.stoplist = StopList()
        self.stoplist.load("./data/stoplist")

    def loadfile(self, path):
        lines = open(path, encoding="latin_1").readlines()
        for line in lines:
            words = [ stem(word.strip()) for word in line.split(" ")
                      if not self.in_stoplist(word.strip()) ]
            self.lines.append(words)

    def in_stoplist(self, word):
        if word == '':
            return True
        return self.stoplist.in_stoplist(word)

    def filter_with_model(self):
        model = Model()
        model.setup()

        lines = []
        for line in self.lines:
            lines.append([word for word in line if model.in_words(word)])
        self.lines = lines

def main():
    pos = BagOfWords()
    pos.loadfile("data/rt-polaritydata/rt-polarity.pos")

    print("===1===")
    print(pos.lines[1:10])
    pos.filter_with_model()

    print("\n===2===")
    print(pos.lines[1:10])

    neg = BagOfWords()
    neg.loadfile("data/rt-polaritydata/rt-polarity.neg")

if __name__ == '__main__':
    main()
