#!/usr/bin/env python

"""
12.  1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したもの
をcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys

"""
cut -f 1
"""
def main():
    file = sys.argv[1]
    lines = open(file).readlines()

    col1 = []
    col2 = []
    for line in lines:
        cols = line.split()
        col1.append(cols[0])
        col2.append(cols[1])

    with open('col1.txt', 'w') as f: f.write('\n'.join(col1) + '\n')
    with open('col2.txt', 'w') as f: f.write('\n'.join(col2) + '\n')

if __name__ == '__main__':
    main()
