#!/usr/bin/env python

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def solve(x, y, z):
    return "%d時の%sは%.1f" % (x, y, z)

if __name__ == '__main__':
    print(solve(12, "気温", 22.4))
