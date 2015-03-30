#!/usr/bin/env python

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，そ
れ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，
長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I
couldn't believe that I could actually understand what I was reading :
the phenomenal power of the human mind ."）を与え，その実行結果を確認
せよ．
"""

import random

def rand(s):
    lis = list(s[1:-1])
    random.shuffle(lis)
    return s[0] + ''.join(lis) + s[-1]

def solve(s):
    res = []
    lis = s.split()
    for w in lis:
        if len(w) >= 4:
            res.append(rand(w))
        else:
            res.append(w)
    return ' '.join(res)


if __name__ == '__main__':
    print(solve("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
