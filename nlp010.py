#!/usr/bin/env python

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

def main():
    file = 'data/hightemp.txt'
    lines = sum(1 for line in open(file))
    print(lines)

if __name__ == '__main__':
    main()
