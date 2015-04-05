#!/usr/bin/env python

"""
48. 名詞から根へのパスの抽出

文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを
抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

import nlp040
import sys

def p(text):
    sys.stdout.write(text)

def main():
    lines = open(sys.argv[1]).readlines()
    text = nlp040.parse_text(lines)

    for sentence in text:
        for i in range(len(sentence)):
            if sentence[i].contains('名詞'):
                out = extract(sentence, i)
                if len(out):
                    p(' -> '.join(out) + '\n')

def extract(sentence, idx):
    out = []
    while True:
        chunk = sentence[idx]
        out.append(chunk.text())
        if sentence[idx].dst <= 0:
            break
        idx = chunk.dst
    if len(out) == 1: out = []
    return out

if __name__ == '__main__':
    main()
