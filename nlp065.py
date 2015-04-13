#!/usr/bin/env python

"""
65. MongoDBの検索

MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関
する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
"""

"""
% mongo nlp
db.artists.find({ "name": "Queen" })
"""

from pymongo import MongoClient

def db():
    client = MongoClient()
    db = client.nlp
    coll = db.artists
    return coll

def main():
    coll = db()
    colls = coll.find({ "name": "Queen" })
    for i, c in enumerate(colls):
        print(i, ":", c, "\n")

if __name__ == '__main__':
    main()
