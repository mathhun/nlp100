#!/usr/bin/env python

"""
56. 共参照解析

Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）
を代表参照表現（representative mention）に置換せよ．ただし，置換すると
きは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように
配慮せよ．
"""

import sys
import xml.etree.ElementTree as etree

class Coreference():
    def __init__(self):
        self.representative = None
        self.mentions = []

    def set_representative(self, mention):
        self.representative = mention

    def append(self, mention):
        self.mentions.append(mention)

    def __repr__(self):
        return '<Coreference r={r} ms={ms}>'.format(r=self.representative, ms=self.mentions)

class Mention():
    def __init__(self):
        self.sentence = -1
        self.start = -1
        self.end = -1
        self.head = -1
        self.text = None
        self.dst = None

    def __repr__(self):
        return '<Mention s={s} st={st} e={e} h={h} t={t} d={d}>'.format(
            s=self.sentence, st=self.start, e=self.end, h=self.head, t=self.text, d=self.dst)

def parse_coref():
    tree = etree.parse(sys.argv[1])
    coref_list = []
    for c in tree.findall('.//coreference/coreference'):
        coref = Coreference()
        for m in c.findall('./mention'):
            mention = Mention()
            if m.attrib.get('representative', 'false') == 'true':
                coref.set_representative(mention)
            else:
                coref.append(mention)
                mention.dst = coref.representative

            mention.sentence = int(m.find('sentence').text)
            mention.start = int(m.find('start').text)
            mention.end = int(m.find('end').text)
            mention.head = int(m.find('head').text)
            mention.text = m.find('text').text

        coref_list.append(coref)
    return coref_list

def replace(coref_list):
    sentences = open('data/out050.txt').readlines()
    for coref in coref_list:
        for m in coref.mentions:
            i = m.sentence - 1
            txt = '{0} ({1})'.format(m.dst.text, m.text)
            sentences[i] = sentences[i].replace(m.text, txt)
    return sentences

if __name__ == '__main__':
    coref_list = parse_coref()
    sentences = replace(coref_list)
    for s in sentences:
        sys.stdout.write(s)
