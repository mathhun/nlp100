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

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X = ngram(2, list(s1))
    Y = ngram(2, list(s2))

    X = set([''.join(x) for x in X])
    Y = set([''.join(y) for y in Y])

    union = X.union(Y)
    inter = X.intersection(Y)
    diff1 = X.difference(Y)
    diff2 = Y.difference(X)

    print(X, ' (X)')
    print(Y, ' (Y)')
    print(union, ' (union)')
    print(inter, ' (intersection)')
    print(diff1, ' (X - Y)')
    print(diff2, ' (Y - X)')

if __name__ == '__main__':
    main()
