#!/usr/bin/env python

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並
び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した
時の結果と合わなくてもよい）．
"""

import sys

"""
sort -k3
"""
def main():
    lines = open(sys.argv[1]).readlines()
    sorted_lines = sorted(lines, key=lambda x: x.split()[2])
    print(sorted_lines)
    for line in sorted_lines:
        sys.stdout.write(line)

if __name__ == '__main__':
    main()
