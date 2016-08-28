#!/usr/bin/env python3

"""word_select

Usage:
    ./word_select.py -i <input> [-o=<number>] [-t <output>]

Examples:
    ./word_select.py -i tst.csv --over 5 --output ed.txt

Options:
    -i --input
    -o --over=<number>           Over number [default: 5]
    -t --output

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='word select 0.1')

import pandas as pd

df = pd.read_csv('%s' % arguments['<input>'])
# print(df)
df1 = df[df.iloc[:, 0] >= int(arguments['--over'])]

if arguments['--output'] == True:
    df1.to_csv(
        '%s' % arguments['<output>'], columns=['Word'], header=None, index=None
        )
    print('Your words are in %s' % arguments['<output>'])
else:
    print(df1)
