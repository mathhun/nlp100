#!/usr/bin/env python

"""
57. 係り受け解析

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向
グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，
Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化する
には，pydotを使うとよい
"""

import sys
import xml.etree.ElementTree as etree

def parse_dependencies():
    tree = etree.parse(sys.argv[1])
    for d in tree.findall('.//dependencies[@type="collapsed-dependencies"]'):
        print(d.tag, d.attrib)

if __name__ == '__main__':
    coref_list = parse_dependencies()
