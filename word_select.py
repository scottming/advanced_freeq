#!/usr/bin/env python3

"""word_select

Usage:
    ./word_select.py -i <input> [-o=<number>] [-d <dic> | -m <meaning>]

Examples:
    ./word_select.py -i tst.csv --over 4 -m meaningfile.md
    ./word_select.py -i tst.csv --over 4 --dic ed.txt

Options:
    -i --input
    -o --over=<number>           Over number [default: 5]
    -d --dic                     For dictionary
    -m --meaning                 Output meaning file

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='word select 0.2')

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
    with open('%s' % arguments['<meaning>'], 'w') as f:
        f.write('\n\n'.join(lst))
    print('Your words_meaning_file are in %s' % arguments['<meaning>'])

elif arguments['--dic'] == True:
    df1.to_csv(
        '%s' % arguments['<dic>'], columns=['Word'], header=None, index=None
        )
    print('Your words are in %s' % arguments['<dic>'])

else:
    print(df1)
