import os
import re
import pandas as pd

dirpath = os.path.dirname(__file__)
CL_PATH = os.path.join(os.path.dirname(__file__),
                       'dictionary/En-Ch_CollinsCOBUILD.txt')

with open(dirpath + '/dictionary/En-Ch_CollinsCOBUILD.txt') as myfile:
    data = myfile.read()

def word_search(data):
    p = re.compile(r'\n\xa0\xa0')
    data1 = p.sub(r'==', data)
    p1 = re.compile(r'\n')
    d = p1.split(data1)
    dic = pd.DataFrame(d, columns=['Meaning'])
    return dic

print(data[:500])
# pattern = arguments['<word>']
# df_search = dic[dic['Meaning'].str.contains(pattern, na=False)]
# lst = list(df_search['Meaning'].values)
# searched = '\n\n'.join(lst)

# p2 = re.compile(r'\xa0\xa0\xa0')
# got = p2.sub(r'\n', searched)
# print(got)
