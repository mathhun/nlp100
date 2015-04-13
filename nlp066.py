#!/usr/bin/env python

"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

"""
% mongo nlp
> db.artists.count({"area":"Japan"})
22821
"""
