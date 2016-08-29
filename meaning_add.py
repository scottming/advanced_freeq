#!/usr/bin/env python
from os.path import expanduser
import pandas as pd
import re

home = expanduser('~')
with open(
    home + '/Dropbox/E.LearningEnglish/Dictionary/En-Ch CollinsCOBUILD.txt'
    ) as myfile:
    data2=myfile.read()

p = re.compile(r'\r\n\r\n\r\n\r\n')
d = p.split(data2)

df = pd.DataFrame(d, columns=['Meaning'])
df['Words'] = df.Meaning.str.extract(r'(★☆☆\s\s\s.*)\r\n').str[12:]
df = df.loc[:, ['Words', 'Meaning']]
print(df.head())