
# coding: utf-8

# In[1]:

import re 
import pandas as pd
import numpy as np


# In[2]:

with open('/home/scott/Dropbox/E.LearningEnglish/Dictionary/En-Ch CollinsCOBUILD.txt') as myfile2:
    data2=myfile2.read()


# In[3]:

# p = re.compile(r'\r\n\r\n\r\n\r\n') # for python2
p = re.compile(r'\n\n\n\n')
# p = re.compile(r'—————————————————')


# In[4]:

d = p.split(data2)


# In[6]:

df = pd.DataFrame(d, columns=['Meaning'])


# In[10]:

df['Word'] = df.Meaning.str.extract(
    '(★☆☆\s\s\s.*)\n');


# In[11]:

df = df.loc[:, ['Word', 'Meaning']]


# In[12]:

f = lambda x: str(x)[6:]


# In[13]:

df['Word'] = df.Word.apply(f)


# In[15]:

df_book = pd.read_csv('tst.csv')


# In[17]:

right = df_book.set_index('Word')


# In[18]:

left = df.set_index('Word')


# In[19]:

df2 = left.join(right)


# In[21]:

df3 = pd.merge(df, df_book, on='Word').sort_values(['Freq', 'Word'], ascending=False)


# In[22]:

VI = df3.Meaning.values


# In[23]:

from io import StringIO


# In[24]:

s = StringIO()


# In[27]:

lst = list(df3.Meaning.values)


# In[30]:

with open('tststr.txt', 'w') as f:
    f.write('\n\n'.join(lst))

