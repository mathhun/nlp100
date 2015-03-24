#!/usr/bin/env python
import pprint
pp = pprint.PrettyPrinter()

def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    lis = s.split()
    idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    dic = {}
    for i in range(len(lis)):
        if i in idx:
            dic[lis[i][0:1]] = i
        else:
            dic[lis[i][0:2]] = i
    pp.pprint(dic)
    return dic

if __name__ == '__main__':
    main()
