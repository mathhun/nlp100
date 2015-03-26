#!/usr/bin/env python

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ
区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ
"""

"""
paste col1.txt col2.txt
"""
def main():
    col1 = open("col1.txt").readlines()
    col2 = open("col2.txt").readlines()

    merged = []
    for i in range(len(col1)):
        merged.append(col1[i].rstrip() + '\t' + col2[i].rstrip())
    with open('col.txt', 'w') as f: f.write('\n'.join(merged) + '\n')

if __name__ == '__main__':
    main()
