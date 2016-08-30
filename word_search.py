#!/usr/bin/env python3

"""word_search

Usage:
    ./word_search.py <word> [-i <input>] [-o <output>]

Examples:
    ./word_search.py 'get'
    ./word_search.py 'get \w*ed'
    ./word_search.py '\doff\d'
    ./word_search.py 'work.*\doff\d'
    ./word_search.py '(walk|walked|walking)(sth|sth.something)\doff\d'

Options:
    -h --help
    -v --versions
    -i --input        Develping...
    -o --output       Develping...

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='word search 0.1')

import pandas as pd
import re

with open('En-Ch CollinsCOBUILD.txt') as myfile:
    data = myfile.read()

p = re.compile(r'\n\xa0\xa0')
data1 = p.sub(r'==', data)
p1 = re.compile(r'\n')
d = p1.split(data1)
dic = pd.DataFrame(d, columns=['Meaning'])

pattern = arguments['<word>']

df_search = dic[dic['Meaning'].str.contains(pattern, na=False)]

lst = list(df_search['Meaning'].values)
searched = '\n\n'.join(lst)

p2 = re.compile(r'\xa0\xa0\xa0')
got = p2.sub(r'\n', searched)
print(got)
