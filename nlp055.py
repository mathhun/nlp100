#!/usr/bin/env python

"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import sys
import xml.etree.ElementTree as etree

def main():
    tree = etree.parse(sys.argv[1])
    for token in tree.findall('.//token'):
        if token.find('NER').text == 'PERSON':
            print(token.find('word').text)

if __name__ == '__main__':
    main()
