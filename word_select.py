#!/usr/bin/env python3

"""word_select

Usage:
    ./word_select.py -i <input> [-o <output>] [-m] [--over=<number>]

Examples:
    ./word_select.py -i tst.csv --over 4 -o  output_fordic.txt
    ./word_select.py -i tst.csv --over 4 -om output_meaningfile.md

Options:
    -h --help           Show this screen
    -v --vesion         Show vesion
    -i --input          Input file of Frequency
    -o --output         Output file
    -m --meaning        Output meaning file
    --over=<number>     Over number [default: 5]

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='word select 0.2')
    print(arguments)
import pandas as pd
import re
import os

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

df = pd.read_csv('%s' % arguments['<input>'])
df1 = df[df.iloc[:, 0] >= int(arguments['--over'])]

if arguments['--meaning'] == True:
    with open(path + '/' + 'En-Ch CollinsCOBUILD.txt') as myfile2:
        data2 = myfile2.read()

    p = re.compile(r'\n\n\n\n')
    d = p.split(data2)
    dic = pd.DataFrame(d, columns=['Meaning'])
    dic['Word'] = dic.Meaning.str.extract('(★☆☆\s\s\s.*)\n', expand=False)

    dic = dic.loc[:, ['Word', 'Meaning']]
    f = lambda x: str(x)[6:]
    dic['Word'] = dic.Word.apply(f)

    mean_data = pd.merge(dic, df1, on='Word').sort_values(
                        ['Freq', 'Word'], ascending=False)
    lst = list(mean_data.Meaning.values)
    with open('%s' % arguments['<output>'], 'w') as f:
        f.write('\n\n'.join(lst))
    print('Your words_meaning_file are in %s' % arguments['<output>'])

elif arguments['--output'] == True:
    df1.to_csv(
        '%s' % arguments['<output>'], columns=['Word'], header=None, index=None
        )
    print('Your words are in %s' % arguments['<output>'])

else:
    print(df1)
