#!/usr/bin/env python
"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

from optparse import OptionParser

"""
split -l
"""
def main():
    parser = OptionParser()
    parser.add_option("-n", None, type="int", dest="nsplit", help="split count")
    (options, args) = parser.parse_args()

    infile = args[0]
    outprefix = args[1]

    lines = open(infile).readlines()
    N = len(lines) // options.nsplit
    width = len(str(options.nsplit))
    outfiles = ["{0}{num:0{width}}".format(outprefix, num=num, width=width) for num in range(options.nsplit)]

    for i in range(options.nsplit):
        out = open(outfiles[i], 'w')
        out.write(''.join(lines[i*N : i*N + N]))

if __name__ == '__main__':
    main()
