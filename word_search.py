
# coding: utf-8

# In[1]:

import pandas as pd
import re


# In[2]:

with open('En-Ch CollinsCOBUILD.txt') as myfile:
    data = myfile.read()


# In[7]:

# p = re.compile(r'==')
#p = re.compile(r'\n')
p = re.compile(r'\n\xa0\xa0')
data1 = p.sub(r'==', data)
p1 = re.compile(r'\n')
d = p1.split(data1)
dic = pd.DataFrame(d, columns=['Meaning'])


# In[36]:

pattern = 'walk.*\soff\s'


# In[37]:

df_search = dic[dic['Meaning'].str.contains(pattern, na=False)]


# In[43]:

lst = list(df_search['Meaning'].values)
searched = '\n\n'.join(lst)


# In[42]:

p2 = re.compile(r'\xa0\xa0\xa0')
got = p2.sub(r'\n', searched)
print(got)

