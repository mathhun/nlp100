#!/usr/bin/env python

"""
44. 係り受け木の可視化

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り
受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向
グラフを直接的に可視化するには，pydotを使うとよい．
"""

import nlp040
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    text = nlp040.parse_text(lines)
    with open(sys.argv[2], 'w') as o:
        i = 0
        o.write('digraph 吾輩は猫である {\n')
        for sentence in text[0:10]:
            o.write('subgraph sentence{0} {{\n'.format(i))
            for chunk in sentence:
                if chunk.dst > 0:
                    o.write('"' + chunk.text() + '" -> "' + sentence[chunk.dst].text() + '";\n')
            o.write('}\n')
            i += 1
        o.write('}\n')

if __name__ == '__main__':
    main()
