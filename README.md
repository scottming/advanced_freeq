## Download


Use Python 3.4+ to get the lastest version of advanced_freeq

```
$ git clone https://github.com/scottming/advanced_freeq.git
```

Decorator packages are required for advanced_freeq.py.

```
$ pip install docopt pdfminer.six numpy pandas
```

### OS X

If you're on Mac OS X, The `sed` will return some error when use `sed -i`, you should use [`Homebrew`](http://brew.sh/) download `gnu-sed` to replace default `sed`.

```
$ brew install gnu-sed --with-default-names
```

Install Calibre

```
$ brew cask install calibre
```

### Debian

```
$ sudo apt-get install calibre
```

## Usage

```
$ ./advanced_freeq.py -h
advanced_freeq

Usage:
    ./advanced_freeq -t <txtname>  [-o <output>] [-s <mastered>]
    ./advanced_freeq -p <pdfname>  [-o <output>] [-s <mastered>]
    ./advanced_freeq -m <mobiname> [-o <output>] [-s <mastered>]
    ./advanced_freeq -e <epubname> [-o <output>] [-s <mastered>]

Examples:
    ./advanced_freeq -i txtname.txt -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv -s mastered.csv

Options:
    -h --help           Show this screen.
    -v --version        Show version
    -t --txt            Input Text file
    -p --pdf            Input PDF file
    -m --mobi           Input mobi file
    -e --epub           Input Epub file
    -o --output         Output frequency file
    -s --mastered       Mastered vocabularies file
```

`mastered.csv` is which vocalubries you have mastered, the default are the top 1000 of [COCA](http://corpus.byu.edu/coca/).

## Thanks to

@[Enaunimes](https://github.com/Enaunimes/freeq); 12dicts word list: <http://wordlist.aspell.net/12dicts-readme/>

lemmas.txt is derrived from 2+2+3lem.txt in version 6 of 12dicts word
list.



