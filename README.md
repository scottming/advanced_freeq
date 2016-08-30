## Download


Use Python 3.4+ to get the lastest version of advanced_freeq

```
$ git clone https://github.com/scottming/advanced_freeq.git
```

Decorator packages are required for advanced_freeq.py.

```
$ pip install docopt pdfminer.six numpy pandas word_cloud image
```

### OS X

If your system is Mac OS X, the `sed` will return some errors when using `sed -i`. You could use  `gnu-sed`  downloaded by [`Homebrew`](http://brew.sh/) to replace the default `sed`

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

### advanced_freeq

```
$ ./advanced_freeq.py -h
advanced_freeq

Usage:
    ./advanced_freeq -i <bookname>  [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]

Examples:
    ./advanced_freeq -i txtname.txt -o bookfreeq.csv
    ./advanced_freeq -i txtname.pdf -o bookfreeq.csv --mas mastered.csv

Options:
    -h --help           Show this screen
    -v --version        Show version
    -i --input          Input file of bookname
    -o --output         Output frequency file
    -c --coca           CoCa Vocabulary
    --mas=<masterted>   Mastered vocabularies file
                        [default: /mastered.csv /COCA_top5000.csv]
						 
```

`mastered.csv` is the vocalubries you have mastered, the default are the top 1000 of [COCA](http://corpus.byu.edu/coca/).

### word_select 

```
$ ./word_select -h
word_select

Usage:
    ./word_select.py -i <input> [-o=<number>] [-d <dic> | -m <meaning>]

Examples:
    ./word_select.py -i tst.csv --over 4 -m meaningfile.md
    ./word_select.py -i tst.csv --over 4 --dic ed.txt

Options:
    -i --input
    -o --over=<number>           Over number [default: 5]
    -d --dic                     For dictionary
    -m --meaning                 Output meaning file

```

### word_cloud

```
$ ./word_cloud -h
word_cloud

Usage:
    ./word_cloud.py -i <input> -o <output>

Examples:
    ./word_cloud.py -i tst.csv -o output.png

Options:
    -i --input
    -o --output
```

### word_search

```
$ ./word_search -h
word_search

Usage:
    ./word_search.py <word> [-i <input>] [-o <output>]

Examples:
    ./word_search.py 'get'
    ./word_search.py 'get \w*ed'
    ./word_search.py '\doff\d'
    ./word_search.py 'work.*\doff\d'
    ./word_search.py '(walk|walked|walking)(sth|sth.something)\doff\d'

Options:
    -h --help
    -v --versions
    -i --input        Develping...
    -o --output       Develping...
```
### Note

If you want to use advanced_free on any local directory, you have to clone this branch, and do: 

```
$ ln -s <yourlocalbranhpath>/advanced_freeq.py ~/usr/local/bin/advanced_freeq
$ ...
```

## Thanks to

@[Enaunimes](https://github.com/Enaunimes/freeq); 12dicts word list: <http://wordlist.aspell.net/12dicts-readme/>

lemmas.txt is derrived from 2+2+3lem.txt in version 6 of 12dicts word
list.



