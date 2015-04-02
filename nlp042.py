#!/usr/bin/env python

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import nlp040
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    text = nlp040.parse_text(lines)

    for sentence in text:
        for chunk in sentence:
            if len(chunk.srcs) > 0:
                txt = ''
                for src in chunk.srcs:
                    txt += sentence[src].text()
                print(txt + '\t' + chunk.text())

if __name__ == '__main__':
    main()
