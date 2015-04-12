#!/usr/bin/env python

"""
64. MongoDBの構築

アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次
のフィールドでインデックスを作成せよ: name, aliases.name, tags.value,
rating.value
"""

import gzip
import json
from pymongo import MongoClient, ASCENDING, DESCENDING

def db():
    client = MongoClient()
    db = client.nlp
    coll = db.artists
    return coll

def mongo_import(artists):
    coll = db()

    for artist in artists:
        coll.insert_one(artist)

def load_artists():
    artists = []
    with gzip.open('data/artist.json.gz', 'rt') as f:
        for line in f:
            artists.append(json.loads(line))
    return artists

def create_index():
    coll = db()
    coll.create_index([("name", ASCENDING)])
    coll.create_index([("aliases.name", ASCENDING)])
    coll.create_index([("tags.value", ASCENDING)])
    coll.create_index([("rating.value", ASCENDING)])

def main():
    #artists = load_artists()
    #mongo_import(artists)
    create_index()

if __name__ == '__main__':
    main()
