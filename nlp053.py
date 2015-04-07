#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import corenlp
from optparse import OptionParser
import re
import xmltodict

def tokenize():
    corenlp_dir = "./lib/stanford-corenlp-full-2015-01-29/"
    #parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    parsed = corenlp.batch_parse('tmp/', corenlp_path=corenlp_dir, raw_output=True)

    for p in parsed:
        text = xmltodict.unparse(p, pretty=True)
        print(text)

def show_words(path):
    with open(path) as f:
        for line in f:
            m = re.search('<word>(.*)</word>', line)
            if m:
                print(m.group(1))

def main():
    parser = OptionParser()
    parser.add_option("-t", "--tokenize", dest="tokenize", default=False)
    parser.add_option("-w", "--word",     dest="word",     default=None)
    (options, args) = parser.parse_args()

    if options.tokenize:
        tokenize()

    if options.word is not None:
        show_words(options.word)

if __name__ == '__main__':
    main()
