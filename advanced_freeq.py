#!/usr/bin/env python3

"""advanced_freeq

Usage:
    ./advanced_freeq -t <txtname>  [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -p <pdfname>  [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -m <mobiname> [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -e <epubname> [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]

Examples:
    ./advanced_freeq -i txtname.txt -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv -c
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv --mas mastered.csv

Options:
    -h --help           Show this screen.
    -v --version        Show version
    -t --txt            Input Text file
    -p --pdf            Isnput PDF file
    -m --mobi           Input mobi file
    -e --epub           Input Epub file
    -o --output         Output frequency file
    -c --coca           CoCa Vocabulary
    --mas=<masterted>   Mastered vocabularies file
                        [default: ~/Documents/GitHubRepoes/advanced_freeq/mastered.csv ~/Documents/GitHubRepoes/advanced_freeq/COCA_top5000.csv]                        

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='advanced freeq 0.3')

import os
import numpy as np
import pandas as pd

if arguments['--txt'] == True:
    os.system(
        'freeq -i %s -o .book_freeq.csv' %
        arguments['<txtname>']
    )
elif arguments['--pdf'] == True:
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
    os.system('freeq -i .book.txt -o .book_freeq.csv')

elif arguments['--mobi'] == True:
    os.system('ebook-convert %s .book.txt' %arguments['<mobiname>'])
    os.system('freeq -i .book.txt -o .book_freeq.csv')

else:
    os.system('ebook-convert %s .book.txt' %arguments['<epubname>'])
    os.system('freeq -i .book.txt -o .book_freeq.csv')

os.system("sed -i 's/^ *//g' .book_freeq.csv")
os.system("sed -i 's/ /,/g' .book_freeq.csv")

df_book = pd.read_csv('.book_freeq.csv', names=['Freq', 'Word'])
f = lambda x: len(str(x)) > 2
df_book = df_book[df_book['Word'].apply(f)]

if arguments['--coca'] == True:
    df_coca = pd.read_csv(
        '%s' % arguments['--mas'][1]
    ).loc[:,['Rank','Word']]
    df_freq = df_book[~df_book['Word'].isin(df_coca['Word'].iloc[:1000])]
    df_freq.to_csv('%s' % arguments['<output>'], index = None)
    print('All your freeq words are in %s' % arguments['<output>'])

else:
    df_mastered = pd.read_csv(
        '%s' % arguments['--mas'][0], names = ['Index', 'Word']
    )
    df_freq = df_book[~df_book['Word'].isin(df_mastered['Word'])]
    df_freq.to_csv('%s' % arguments['<output>'], index = None)
    print('All your word frequency are in %s' % arguments['<output>'])
