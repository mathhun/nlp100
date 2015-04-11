#!/usr/bin/env python

"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

import gzip
import json
import redis

def redis_import(artists):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for artist in artists:
        if artist.get('name', False):
            print(artist['name'], artist.get('area', None))
            r.set(artist['name'], artist.get('area', None))

def main():
    artists = []
    with gzip.open('data/artist.json.gz', 'rt') as f:
        for line in f:
            artists.append(json.loads(line))
    redis_import(artists)

if __name__ == '__main__':
    main()
