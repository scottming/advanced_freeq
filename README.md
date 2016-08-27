## Download


Use Python 3.4+ to get the lastest version of advanced_freeq

```
git clone https://github.com/scottming/advanced_freeq.git
```

Decorator packages are required for advanced_freeq.py.

```
pip install docopt pdfminer.six numpy pandas
```


## Usage

```
$ ./advanced_freeq.py -h
advanced_freeq

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
```

`mastered.csv` is which vocalubries you have mastered, the default are the top 1000 of [COCA](http://corpus.byu.edu/coca/).

## Thanks to

@[Enaunimes](https://github.com/Enaunimes/freeq); 12dicts word list: <http://wordlist.aspell.net/12dicts-readme/>

lemmas.txt is derrived from 2+2+3lem.txt in version 6 of 12dicts word
list.



