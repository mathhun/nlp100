#!/usr/bin/env python

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import nlp030
import sys

def main(path):
    parsed = nlp030.mecab(path)
    for sentence in parsed:
        for i in range(len(sentence)):
            try:
                if sentence[i]['surface'] == 'の':
                    if sentence[i-1]['pos'] == '名詞' and sentence[i+1]['pos'] == '名詞':
                        print(sentence[i-1]['surface'] + 'の' + sentence[i+1]['surface'])
            except IndexError:
                pass
                        

if __name__ == '__main__':
    main(sys.argv[1])
