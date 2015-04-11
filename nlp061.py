#!/usr/bin/env python

"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

import redis
import sys

def main():
    key = sys.argv[1]
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    for name in sorted(r.keys('*' + key + '*'), key=lambda x: x.decode('utf-8').lower()):
        print(name.decode('utf-8') + '\t' + r.get(name).decode('utf-8'))

if __name__ == '__main__':
    main()
