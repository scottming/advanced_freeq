#!/usr/bin/env python3
import numpy as np
import pandas as pd

df = pd.read_csv('../out.csv')
df = df[['Word','Freq']]
tuples = [tuple(x) for x in df.values]

from os import path
from wordcloud import WordCloud

d = path.dirname('__file__')

# Generate a word cloud image
wordcloud = WordCloud().generate_from_frequencies(tuples)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate_from_frequencies(tuples)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
