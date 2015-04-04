#!/usr/bin/env python

"""
46. 動詞の格フレーム情報の抽出

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文
節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を
満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
"""

import nlp040
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    text = nlp040.parse_text(lines)

    with open(sys.argv[2], 'w') as o:
        for sentence in text:
            for chunk in sentence:
                for x in chunk.get('動詞'):
                    ys = []
                    zs = []
                    for src in chunk.srcs:
                        for y in sentence[src].get('助詞'):
                            ys.append(y.base)
                            zs.append(sentence[src].text())
                    if len(ys) > 0:
                        lis = sorted(zip(ys, zs), key=lambda x: x[0])
                        ys = [ x[0] for x in lis ]
                        zs = [ x[1] for x in lis ]
                        o.write(x.base + '\t' + ' '.join(ys) + '\t' + ' '.join(zs) + '\n')

if __name__ == '__main__':
    main()
