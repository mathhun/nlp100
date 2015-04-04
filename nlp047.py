#!/usr/bin/env python

"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
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
                    w = ''
                    for src in chunk.srcs:
                        # 返事を
                        for i in range(len(sentence[src].morphs) - 1):
                            morph1 = sentence[src].morphs[i]
                            morph2 = sentence[src].morphs[i+1]
                            if morph1.pos1 == 'サ変接続' and morph2.surface == 'を':
                                w = sentence[src].text()

                    if w == '': continue

                    ys = []
                    zs = []
                    for src in chunk.srcs:
                        # 及ぼさんと 手紙に
                        for y in reversed(sentence[src].get('助詞')):
                            ys.append(y.base)
                            zs.append(sentence[src].text())
                            break
                                
                    if len(ys) > 0:
                        lis = sorted(zip(ys, zs), key=lambda x: x[0])
                        ys = [ x[0] for x in lis ]
                        zs = [ x[1] for x in lis ]
                        o.write(w + x.base + '\t' + ' '.join(ys) + '\t' + ' '.join(zs) + '\n')
                    break

if __name__ == '__main__':
    main()

"""
% cut -f1 tmp/ans047 | sort | uniq -c | sort -nr | head -n20
  29 返事をする
  21 挨拶をする
  14 真似をする
  14 話をする
  11 喧嘩をする
   8 質問をする
   7 運動をする
   6 昼寝をする
   6 話を聞く
   5 質問をかける
   5 相談をする
   5 病気をする
   5 注意をする
   5 問答をする
   4 いたずらをする
   4 御辞儀をする
   4 休養を要する
   4 演説をする
   4 欠伸をする
   3 一大活躍を試みる

% awk -F"\t" '{print $1, $2}' tmp/ans047 | sort | uniq -c | sort -nr | head -n20
   8 真似をする を
   6 返事をする と を
   6 運動をする を
   4 挨拶をする から を
   4 返事をする と は を
   4 挨拶をする と を
   4 返事をする を
   4 喧嘩をする を
   4 話を聞く を
   3 質問をかける と は を
   3 喧嘩をする と を
   3 話をする を
   2 御無沙汰をする を
   2 いたずらをする を
   2 同情を表する て と は を
   2 休養を要する は を
   2 深入りをする を
   2 返事をする から と を
   2 挨拶をする と も を
   2 議論をする て を
"""
