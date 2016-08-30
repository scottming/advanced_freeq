#!/usr/bin/env python3

"""word_cloud

Usage:
    ./word_cloud.py -i <input> -o <output>

Examples:
    ./word_cloud.py -i tst.csv -o output.png

Options:
    -i --input
    -o --output

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='word cloud 0.1')
    print(arguments)

import pandas as pd

df = pd.read_csv('%s' % arguments['<input>'])
df = df[['Word','Freq']]
tuples = [tuple(x) for x in df.values]

from wordcloud import WordCloud

# Generate a word cloud image
wordcloud = WordCloud().generate_from_frequencies(tuples)

# Display the generated image:
import matplotlib.pyplot as plt

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(
            max_font_size=60, relative_scaling=.5
            ).generate_from_frequencies(tuples)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('%s' % arguments['<output>'], dpi=300)
plt.show()
