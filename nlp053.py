#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import corenlp
import xmltodict

def main():
    corenlp_dir = "./lib/stanford-corenlp-full-2015-01-29/"
    #parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    parsed = corenlp.batch_parse('tmp/', corenlp_path=corenlp_dir, raw_output=True)

    for p in parsed:
        text = xmltodict.unparse(p, pretty=True)
        print(text)

if __name__ == '__main__':
    main()
