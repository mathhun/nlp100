#!/usr/bin/env python
"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import re
import sys

"""
gsed -e 's/\t/ /g'
"""
def main():
    lines = sys.stdin.readlines()
    lines = [re.sub('\t', ' ', line) for line in lines]
    sys.stdout.writelines(lines)

if __name__ == '__main__':
    main()
