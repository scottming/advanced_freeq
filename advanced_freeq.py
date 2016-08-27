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
import numpy as np
import pandas as pd

if arguments['--pdf'] == True:
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    from io import StringIO

    def convert_pdf_to_txt(path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        with open('.book.txt', 'w') as book:
            book.write('%s' % str)
    convert_pdf_to_txt(arguments['<pdfname>'])
    os.system('./freeq.py -i .book.txt -o .book_freeq.csv')

else:
    os.system(
        './freeq -i %s -o .book_freeq.csv' %
        arguments['<bookname>']
    )

os.system("sed -i 's/^ *//g' .book_freeq.csv")
os.system("sed -i 's/ /,/g' .book_freeq.csv")

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
