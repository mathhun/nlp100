#!/usr/bin/env python

"""
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""

import random

def main():
    pos = open("./data/rt-polaritydata/rt-polarity.pos", encoding="latin_1").readlines()
    neg = open("./data/rt-polaritydata/rt-polarity.neg", encoding="latin_1").readlines()

    pos = ["+1 " + line for line in pos]
    neg = ["-1 " + line for line in neg]

    lines = pos + neg
    random.shuffle(lines)

    with open("./data/sentiment.txt", "w") as o:
        for line in lines:
            o.write(line)

if __name__ == '__main__':
    main()
