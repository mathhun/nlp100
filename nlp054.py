#!/usr/bin/env python

"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ
"""

import sys
import xml.etree.ElementTree as etree

def main():
    tree = etree.parse(sys.argv[1])
    for token in tree.findall('//token'):
        print('\t'.join([token.find('word').text, token.find('lemma').text, token.find('POS').text]))

if __name__ == '__main__':
    main()
