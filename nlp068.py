#!/usr/bin/env python

"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
"""

"""
db.artists.find({'tags.value':'dance'}).sort({'rating.value':-1}).limit(10)
"""
