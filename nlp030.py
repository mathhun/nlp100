#!/usr/bin/env python

"""
第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態
素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイ
ルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

----------------------------------------------------------------------

30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，
各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1
（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）
のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラム
を活用せよ．

0,      1,  2,   3,   4,       7,
surface,pos,pos1,pos2,pos3,    base
吾輩    名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
猫      名詞,一般,*,*,*,*,猫,ネコ,ネコ
で      助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある    助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
。      記号,句点,*,*,*,*,。,。,。
EOS

[
  [
    {surface=>xxx, },
    {surface=>yyy, },
    :
  ],
  :
]
"""

import sys

def parse_line(line):
    parsed = {}

    if line.strip() == "EOS":
        return line

    surface, rest = line.split('\t', 1)
    rest = rest.split(',')

    parsed['surface'] = surface
    parsed['pos']  = rest[0]
    parsed['pos1'] = rest[1]
    parsed['base'] = rest[6]

    return parsed

def mecab(path):
    with open(path) as f:
        text = []
        sentence = []
        for line in f:
            if line.strip() == "EOS":
                if len(sentence) > 0:
                    text.append(sentence[:])
                    sentence = []
            else:
                parsed = parse_line(line)
                sentence.append(parsed)
        return text

if __name__ == '__main__':
    print(mecab(sys.argv[1]))
