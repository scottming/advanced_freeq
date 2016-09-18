import click
import re
import string
import sys
import os
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if sys.version_info[0] > 2:
    from io import StringIO
else:
    from io import BytesIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

dirpath = os.path.dirname(__file__)


def pdf_to_txt(input_book, name):
    rsrcmgr = PDFResourceManager()
    try:
        retstr = StringIO()
    except NameError:
        retstr = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(input_book, 'rb')
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
    with open(name + '.txt', 'w') as book:
        book.write('%s' % str)


def other_format_to_txt(input_book):
    os.system('ebook-convert %s .txt' % input_book)


lemmas = {}
LEM_PATH = os.path.join(os.path.dirname(__file__),
                       'lemmas.txt')
with open(LEM_PATH) as fin:
    for line in fin:
        line = line.strip()
        headword = line.split('\t')[0]
        try:
            related = line.split('\t')[1]
        except IndexError:
            related = None
        lemmas[headword] = related


valid_words = set()
for headword, related in lemmas.items():
    valid_words.add(headword)
    if related:
        valid_words.update(set(related.split()))


class WordFinder(object):
    '''A compound structure of dictionary and set to store word mapping'''
    def __init__(self):
        """Initialize lame containers for 'quick' search

        Structure of main_table
        {
            'a':{
                     # All related words and the headword start with same letter
                     'abandon': {'abandons', 'abandoned', 'abandoning'},

                     'apply': {'applies', 'applied', 'applying'},

                     # headword with no related word
                     'abeam': None,
                     ...
                },
            'b': {...},
            'c': {...},
            ...
        }

        Structure of special_table
        {

            # 1+ related words does not share the same starting letter
            # with heasdword
            'although': {'altho', 'tho', 'though'},
            'bad': {'badder', 'baddest', 'badly', 'badness', 'worse', 'worst'},
            ...
        }

        """
        self.main_table = {}
        for char in string.ascii_lowercase:
            self.main_table[char] = {}
        self.special_table = {}

        for headword, related in lemmas.items():
            # Only 3 occurrences of uppercase in lemmas.txt, which include 'I'
            # Trading precision for simplicity
            headword = headword.lower()
            try:
                related = related.lower()
            except AttributeError:
                related = None
            if related:
                for word in related.split():
                    if word[0] != headword[0]:
                        self.special_table[headword] = set(related.split())
                        break
                else:
                    self.main_table[headword[0]][headword] = set(related.split())
            else:
                self.main_table[headword[0]][headword] = None

    def find_headword(self, word):
        """Search the 'table' and return the original form of a word"""
        word = word.lower()
        alpha_table = self.main_table[word[0]]
        if word in alpha_table:
            return word

        for headword, related in alpha_table.items():
            if related and (word in related):
                return headword

        for headword, related in self.special_table.items():
            if word == headword:
                return word
            if word in related:
                return headword
        # This should never happen after the removal of words not in valid_words
        # in Book.__init__()
        return None

    # TODO
    def find_related(self, headword):
        pass


def is_dirt(word):
    return word not in valid_words


def list_dedup(list_object):
    """Return the deduplicated copy of given list"""
    temp_list = []
    for item in list_object:
        if item not in temp_list:
            temp_list.append(item)
    return temp_list


class Book(object):
    def __init__(self, filepath):
        with open(filepath) as bookfile:
            content = bookfile.read().lower()
            self.temp_list = re.split(r'\b([a-zA-Z-]+)\b', content)
            self.temp_list = [item for item in self.temp_list if not is_dirt(item)]
            finder = WordFinder()
            self.temp_list = [finder.find_headword(item) for item in self.temp_list]

    def freq(self):
        """Count word frequencies and return a collections.Counter object"""
        cnt = Counter()
        for word in self.temp_list:
            cnt[word] += 1
        return cnt

    # TODO
    def stat(self):
        pass


class Op(object):
    '''Option Class'''
    def __init__(self, inputfile, mastered=None,
                 s=None, name=None, fomat=None):
        self.inputfile = inputfile
        self.mastered = mastered
        self.s = self.inputfile.split('.')
        self.name = '.'.join(self.s[:-1]) # bookname
        self.fomat = self.s[-1] # bookformat


def get_freq(input_txt):
    '''Input file with TXT format'''
    book = Book(input_txt)
    result = book.freq()

    report = ['Freq,Word']
    for word in sorted(result, key=lambda x: result[x], reverse=True):
        report.append('{},{}'.format(result[word], word))

    LINE_SEP = os.linesep
    return LINE_SEP.join(report)


def clear_word(input_freq, mastered):
    df_book = pd.read_csv(input_freq)
    f = lambda x: len(str(x)) > 2
    df_book = df_book[df_book['Word'].apply(f)]
    df_mastered = pd.read_csv(mastered)
    df_freq = df_book[~df_book['Word'].isin(df_mastered['Word'])]
    return df_freq


try:
    outcsv = StringIO()
except NameError:
    outcsv = BytesIO()

def determine_fomat(inputfile, name, fomat, mastered):
    if fomat == 'pdf':
        pdf_to_txt(inputfile, name)
    elif fomat == 'txt':
        pass
    else:
        other_format_to_txt(inputfile)

    meta_freq = get_freq(name + '.txt')
    outcsv.write(meta_freq)
    outcsv.seek(0)
    freq = clear_word(outcsv, mastered)
    return freq


COL_PATH = os.path.join(os.path.dirname(__file__),
                       'dictionary/En-Ch_CollinsCOBUILD.txt')
with open(COL_PATH) as myfile:
        col_data = myfile.read()
def find_col_mean(dic_data, freq_data):

    p = re.compile(r'\n\n\n\n')
    d = p.split(dic_data) # apply words
    df_dic = pd.DataFrame(d, columns=['Meaning'])
    df_dic['Word'] = df_dic.Meaning.str.extract('(★☆☆\s\s\s.*)\n', expand=False)  # extract the words line

    df_dic = df_dic.loc[:, ['Word', 'Meaning']]
    f = lambda x: str(x)[6:]
    df_dic['Word'] = df_dic.Word.apply(f)  # deep extract

    mean_data = pd.merge(df_dic, freq_data, on='Word').sort_values(
                        ['Freq', 'Word'], ascending=False)
    lst = list(mean_data.Meaning.values)
    return lst


OXF_PATH = os.path.join(os.path.dirname(__file__),
                       'dictionary/En-Ch_Oxford_Advanced_Leaners_Dictionary.txt')
with open(OXF_PATH) as myfile1:
        oxf_data = myfile1.read()
def find_oxf_mean(dic_data, freq_data):

    p = re.compile(r'\n\n\n')
    d = p.split(dic_data) # apply words
    df_dic = pd.DataFrame(d, columns=['Meaning'])
    df_dic['Word'] = df_dic.Meaning.str.extract('(★☆☆\s\s\s.*)\n', expand=False)  # extract the words line

    df_dic = df_dic.loc[:, ['Word', 'Meaning']]
    f = lambda x: str(x)[6:]
    df_dic['Word'] = df_dic.Word.apply(f) # deep extract

    mean_data = pd.merge(df_dic, freq_data, on='Word').sort_values(
                        ['Freq', 'Word'], ascending=False)
    lst = list(mean_data.Meaning.values)
    return lst

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-i', '--inputfile')
@click.option('-m', '--mastered', default=dirpath + '/mastered.csv')
@click.pass_context
def cli(ctx, inputfile, mastered):
    '''freeq is a script to generate word frequency report of English text/pdf/epub...

    Example:

    \b
        freeq -i tsttxt.pdf dic
        freeq -i tstpdf.txt mean

    \b
        freeq -i tsttxt.txt dic  -o out.txt
        freeq -i tstpdf.pdf mean -o out.txt

    \b
        freeq -i tsttxt.txt dic  -n 2 -o out.txt
        freeq -i tstpdf.pdf meen -n 2 -o out.txt
    '''
    ctx.obj = Op(inputfile, mastered)


@cli.command()
@click.option('-o', '--output')
@click.option('-n', '--number', default=3, help='Over freq number.')
@click.pass_obj
def read(ctx, output, number):
    '''Get a frequency for read.'''
    freq = determine_fomat(ctx.inputfile, ctx.name,
                           ctx.fomat, ctx.mastered)
    freq = freq[freq.loc[:, 'Freq'] > number]
    if output != None:
        freq.to_csv(output, index=False)
    else:
        print(freq)


@cli.command()
@click.option('-o', '--output')
@click.option('-n', '--number', default=3, help='Over freq number.')
@click.pass_obj
def dic(ctx, output, number):
    '''Get a frequency to dictionary, like EuDic.'''
    freq = determine_fomat(ctx.inputfile, ctx.name,
                           ctx.fomat, ctx.mastered)
    freq = freq[freq.loc[:, 'Freq'] > number]
    if output != None:
        freq.to_csv(output, index=False,
                     header=None, columns=['Word'])
    else:
        print(freq['Word'])


@cli.command()
@click.option('-o', '--output')
@click.option('-n', '--number', default=3, help='Over freq number.')
@click.pass_obj
def cloud(ctx, output, number):
    '''Get a wordcloud image.'''
    freq = determine_fomat(ctx.inputfile, ctx.name,
                           ctx.fomat, ctx.mastered)
    freq = freq[freq.loc[:, 'Freq'] > number]
    freq = freq[['Word', 'Freq']]
    tuples = [tuple(x) for x in freq.values]
    wordcloud = WordCloud(
                max_font_size=60, relative_scaling=.5
                ).generate_from_frequencies(tuples)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    if output != None:
        plt.savefig(output, dpi=300)
    else:
        plt.show()


@cli.command()
@click.option('-o', '--output')
@click.option('-n', '--number', default=3, help='Over freq number.')
@click.option('--dic', type=click.Choice(['oxf','col']),
              default='oxf', help='Choice the dictionary.')
@click.pass_obj
def mean(ctx, output, number, dic):
    '''Get the mean of freq words from dictionary.'''
    freq = determine_fomat(ctx.inputfile, ctx.name,
                           ctx.fomat, ctx.mastered)
    freq = freq[freq.loc[:, 'Freq'] > number]
    if dic == 'oxf':
        lst = find_oxf_mean(oxf_data, freq)
        if output != None:
            with open(output, 'w') as file:
                file.write('\n\n'.join(lst))
        else:
            print('\n\n'.join(lst))
    else:
        lst = find_col_mean(col_data, freq)
        if output != None:
            with open(output, 'w') as file:
                file.write('\n\n'.join(lst))
        else:
            print('\n\n'.join(lst))


cli()

