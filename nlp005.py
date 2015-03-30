#!/usr/bin/env python

def ngram(n, lis):
    ngram_array = []
    for i in range(len(lis)):
        ary = []
        for j in range(n):
            try:
                ary.append(lis[i + j])
            except IndexError:
                pass
        ngram_array.append(ary)
    return ngram_array

if __name__ == '__main__':
    import re
    print(ngram(2, list(re.sub(r' ', '', "I am an NLPer"))))
    print(ngram(2, "I am an NLPer".split()))
