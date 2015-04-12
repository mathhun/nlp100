#!/usr/bin/env python

"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import redis

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    artists = r.keys('*')
    areas = r.mget(artists)
    japanese = []
    for artist, area in zip(artists, areas):
        if area == b'Japan':
            japanese.append(artist.decode('utf-8'))

    print(japanese)
    print(len(japanese))

if __name__ == '__main__':
    main()
