#!/usr/bin/env python3

"""advanced_freeq

Usage:
    ./advanced_freeq (-i <bookname> | -p <pdfname>)  [-o <output>] [-m <mastered>]

Examples:
    ./advanced_freeq -i bookname.txt -o bookfreeq.csv
    ./advanced_freeq -p bookname.pdf -o bookfreeq.csv
    ./advanced_freeq -p bookname.pdf -o bookfreeq.csv -m mastered.csv

Options:
    -h --help           Show this screen.
    -v --version        Show version
    -i --input          Input Text file
    -p --pdf            Input PDF file
    -o --output         Output frequency file
    -m --mastered       Mastered vocabularies file
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='advanced freeq 0.1')

import os

if arguments['--pdf'] == True:
    os.system('pdf2txt %s > .book.txt' % arguments['<pdfname>'])
    os.system(
        './freeq.py -i .book.txt -o .book_freeq.csv'
    )

else:
    os.system(
        './freeq.py -i %s -o .book_freeq.csv' %
        arguments['<bookname>']
    )

os.system("sed -i 's/^ *//g' .book_freeq.csv")
os.system("sed -i 's/ /,/g' .book_freeq.csv")

import numpy as np
import pandas as pd

df_book = pd.read_csv('.book_freeq.csv', names=['Freq', 'Word'])

if arguments['--mastered'] == False:
    df_coca = pd.read_csv(
        'COCA_top5000.csv'
    ).loc[:,['Rank','Word']]
    df_freq = df_book[~df_book['Word'].isin(df_coca['Word'].iloc[:1000])]
    df_freq.to_csv('%s' % arguments['<output>'], index = None)
    print('All your freeq words are in %s' % arguments['<output>'])

else:
    df_mastered = pd.read_csv(
        '%s' % arguments['<mastered>'], names = ['Index', 'Word']
    )
    df_freq = df_book[~df_book['Word'].isin(df_mastered['Word'])]
    df_freq.to_csv('%s' % arguments['<output>'], index = None)
    print('All your word frequency are in %s' % arguments['<output>'])
