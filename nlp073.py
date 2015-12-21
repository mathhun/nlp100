#!/usr/bin/env python

"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

import numpy as np
import pandas as pd
import re, sys
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix

pos = open("./data/rt-polaritydata/rt-polarity.pos", encoding="latin_1").readlines()
neg = open("./data/rt-polaritydata/rt-polarity.neg", encoding="latin_1").readlines()

lenp = len(pos)
lenn = len(pos)

vectorizer = CountVectorizer(min_df=1)

X_pos = vectorizer.fit_transform(pos)
X_neg = vectorizer.fit_transform(neg)
print(X_pos)
sys.exit()

stoplist = [
    "a", "the", ".", '"', "'", ",", ";", ":", "--", "(", ")"
    "i", "my", "me", "mine",
    "he", "his", "him", "he's",
    "she", "her", "hers",
    "we", "our", "us", "ours",
    "it", "it's",
    "be", "are", "is", "was", "were",
    "in", "of", "with"
]

#words = []
# for line in pos:
#     for word in re.compile(r'[ \t\n]').split(line):
#         word = word.strip().lower()
#         if word in stoplist or len(word) == 0:
#             pass
#         else:
#             words.append(word)
# print(len(words))
    
df_pos = pd.DataFrame({ 'label': np.array([1]  * lenp), 'text': X_pos.toarray() })
df_neg = pd.DataFrame({ 'label': np.array([-1] * lenn), 'text': X_neg.toarray() })
df = pd.concat([df_pos, df_neg])
print(df)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

model = LogisticRegression(C=1e5)
model.fit(X_train, y_train)

#pred = model.predict(X_test)

#cm = confusion_matrix(y_test, pred)
#print(cm)
