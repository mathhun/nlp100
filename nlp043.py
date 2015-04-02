#!/usr/bin/env python

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

import nlp040
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    text = nlp040.parse_text(lines)
    for sentence in text:
        for chunk in sentence:
            if len(chunk.srcs) > 0 and chunk.contains('動詞') \
               and any([sentence[idx].contains('名詞') for idx in chunk.srcs]):
                txt = ''
                for src in chunk.srcs:
                    txt += sentence[src].text()
                print(txt + '\t' + chunk.text())

if __name__ == '__main__':
    main()
