#!/usr/bin/env python

"""
20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を
表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
import re
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    jsons = [json.loads(line) for line in lines]
    texts_british = [js['text'] for js in jsons if re.search('イギリス', js['text'])]
    for text in texts_british:
        sys.stdout.write(text)

if __name__ == '__main__':
    main()
