#!/usr/bin/env python

"""
>>> solve()
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
"""
def solve():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    lis = re.sub(r'[,.]', '', s).split()
    return [ n for n in map(lambda x: len(x), lis) ]

if __name__ == '__main__':
    import re
    from functools import reduce
    import doctest
    doctest.testmod()
