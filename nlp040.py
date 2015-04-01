#!/usr/bin/env python

"""第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係
り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．この
ファイルを用いて，以下の問に対応するプログラムを実装せよ．

40. 係り受け解析結果の読み込み（形態素）

形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本
形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととす
る．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文を
Morphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

41. 係り受け解析結果の読み込み（文節・係り受け）

40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morph
オブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェ
クトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章
の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import re
import sys

class Chunk:
    def __init__(self):
        self.index = None
        self.dst = None
        self.srcs = []
        self.morphs = []

    def append(self, morph):
        self.morphs.append(morph)

    def __str__(self):
        ms = []
        for m in self.morphs:
            ms.append(m.__str__())
        ms = ','.join(ms)
        return "<chunk i={0} d={1} s={2} ms={3}".format(self.index, self.dst, self.srcs, ms)

    def __repr__(self):
        return self.__str__()

class Morph:
    def __init__(self):
        self.surface = None
        self.base = None
        self.pos = None
        self.pos1 = None

    def __str__(self):
        return "<{0}>".format(self.surface)

    def __repr__(self):
        return self.__str__()


def parse_text(lines):
    i = 0
    l = len(lines)
    text = []
    sentence = []
    chunk = None

    while i < l:
        if lines[i].strip() == 'EOS':
            if len(sentence) > 0:
                calc_srcs(sentence)
                text.append(sentence)
            sentence = []
        else:
            if re.match('\* \d+ -?\d+D', lines[i]):
                chunk = parse_chunk_header(lines[i])
                sentence.append(chunk)
            else:
                morph = parse_morph(lines[i])
                chunk.append(morph)
        i += 1

    return text

def calc_srcs(sentence):
    for chunk in sentence:
        if chunk.dst > 0:
            sentence[chunk.dst].srcs.append(chunk.index)

def parse_chunk_header(line):
    m = re.match('\* (\d+) (-?\d+)D (\d+/\d+) (-?[.0-9]+)', line)
    if m:
        chunk = Chunk()
        chunk.index = int(m.group(1))
        chunk.dst   = int(m.group(2))
        return chunk
    else:
        raise Exception('parse error: ' + line)

def parse_morph(line):
    w, rest = line.split('\t', 1)
    rest = rest.split(',')

    morph = Morph()
    morph.surface = w
    morph.pos  = rest[0]
    morph.pos1 = rest[1]
    morph.base = rest[6]

    return morph

if __name__ == '__main__':
    lines = open(sys.argv[1]).readlines()
    text = parse_text(lines)

    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(text)
