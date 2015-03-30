#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
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
            txt = strip_mediawiki_markup(m.group(2).strip())
            dic[m.group(1).strip()] = txt
        else:
            sys.stderr.write('Parse error: {0}'.format(line))
    return dic

def strip_mediawiki_markup(text):
    text = re.sub("''(.*?)''", r"\1", text)
    text = re.sub("'''(.*?)'''", r"\1", text)
    text = re.sub("'''''(.*?)'''''", r"\1", text)
    return text

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
