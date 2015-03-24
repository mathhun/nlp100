#!/usr/bin/env python

"""
>>> solve()
'パタトクカシーー'
"""
def solve():
    str = ""
    for a, b in zip("パトカー", "タクシー"):
        str += a + b
    return str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
