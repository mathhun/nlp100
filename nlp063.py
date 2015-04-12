#!/usr/bin/env python

"""
63. オブジェクトを値に格納したKVS

KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回
数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築
したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""

import gzip
import json
import redis
import sys

def build():
    artists = []
    with gzip.open('data/artist.json.gz', 'rt') as f:
        for line in f:
            artists.append(json.loads(line))

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for artist in artists:
        if artist.get('name', False):
            #print(artist['name'], artist.get('tags', {}))
            r.set(artist['name'], artist.get('tags', {}))

def search(key):
    print("key=",key)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    for name in sorted(r.keys('*' + key + '*'), key=lambda x: x.decode('utf-8').lower()):
        print(name.decode('utf-8') + '\t' + r.get(name).decode('utf-8'))

def main():
    subcommand = sys.argv[1]
    if subcommand == "build":
        build()
    elif subcommand == "search":
        search(sys.argv[2])
    else:
        raise Exception("invalid input")

if __name__ == '__main__':
    main()
