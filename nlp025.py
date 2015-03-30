#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""
import pprint
import re
import sys

def parse_template(text):
    #m = re.match('\A{{ ([^\|]+) ( \s* \|  \s* (.*?) \s* )+ }}\Z', text, flags=re.X|re.S)
    m = re.match('\A{{ (.*?) \s* \| \s* (.*) }}\Z', text, flags=re.X|re.M|re.S)
    if m is None:
        raise Exception('Invalid format')

    dic = {}
    lines = m.group(2).splitlines() # assume 1 line 1 key&value...
    for line in lines:
        m = re.match('\s* \|? \s* ([^\|]+) \s* = \s* (.*) \s* \|? \s*', line, flags=re.X)
        if m:
            dic[m.group(1).strip()] = m.group(2).strip()
        else:
            sys.stderr.write('Parse error: {0}'.format(line))
    return dic

def main():
    pp = pprint.PrettyPrinter()
    lines = open(sys.argv[1], encoding='UTF-8').readlines()
    text = ''.join(lines)
    matches = re.findall('{{基礎情報.*?^}}', text, flags=re.M|re.S)
    for match in matches:
        template = parse_template(match)
        pp.pprint(template)

if __name__ == '__main__':
    main()
