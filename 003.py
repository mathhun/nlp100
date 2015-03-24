#!/usr/bin/env python

#from functools import reduce

def main():
    lis = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split()
    lis = [ n for n in map(lambda x: len(x), lis) ]
    print(lis)

if __name__ == '__main__':
    main()
