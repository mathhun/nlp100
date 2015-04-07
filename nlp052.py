#!/usr/bin/env python

"""
52. ステミング

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミング
アルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

import re
from stemming.porter2 import stem
import sys

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip('\n')
            w = re.sub('[.,:;!\?"]', '', line)
            w = stem(w)
            sys.stdout.write(line + '\t' + w + '\n')

if __name__ == '__main__':
    main()
