## Download


Use Python 3.4+ to get the lastest version of advanced_freeq

```
git clone https://github.com/scottming/advanced_freeq.git
```

Decorator packages are required for advanced_freeq.py.

```
pip install docopt pdfminer.six numpy pandas
```

### OS X

If you're on Mac OS X, The `sed` will return some error when use `sed -i`, you should use [`Homebrew`](http://brew.sh/) download `gnu-sed` to replace default `sed`.

```
brew install gnu-sed --with-default-names
```

Install Calibre

```
brew cask install calibre
```

### Debian

```
sudo apt-get install calibre
```

## Usage

```
$ ./advanced_freeq.py -h
advanced_freeq

Usage:
    ./advanced_freeq -t <txtname>  [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -p <pdfname>  [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -m <mobiname> [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]
    ./advanced_freeq -e <epubname> [-o <output>] [-c] [--mas=<mastered> --mas=<mastered>]

Examples:
    ./advanced_freeq -i txtname.txt -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv -c
    ./advanced_freeq -p txtname.pdf -o bookfreeq.csv --mas mastered.csv

Options:
    -h --help           Show this screen.
    -v --version        Show version
    -t --txt            Input Text file
    -p --pdf            Isnput PDF file
    -m --mobi           Input mobi file
    -e --epub           Input Epub file
    -o --output         Output frequency file
    -c --coca           CoCa Vocabulary
    --mas=<masterted>   Mastered vocabularies file
                        [default: ~/Documents/GitHubRepoes/advanced_freeq/mastered.csv ~/Documents/GitHubRepoes/advanced_freeq/COCA_top5000.csv]
						 
```

`mastered.csv` is which vocalubries you have mastered, the default are the top 1000 of [COCA](http://corpus.byu.edu/coca/).

```
word_select

Usage:
    ./word_select.py -i <input> [-o=<number>] [-t <output>]

Examples:
    ./word_select.py -i tst.csv --over 5 --output ed.txt

Options:
    -i --input
    -o --over=<number>  Over number [default: 5]
    -t --output
```

If you want to use advanced_free on any local directory, you have to clone this branch, and change something

```
ln -s <yourlocalbranhpath>/freeq.py ~/.bin/freeq
ln -s <yourlocalbranhpath>/advanced_freeq.py ~/.bin/advanced_freeq
```

In `freeq.py`

```git
-with open('/Users/Scott/Documents/GitHubRepoes/advanced_freeq/lemmas.txt') as f
+with open('<yourlocalRepositoryPath>/advanced_freeq/lemmas.txt') as f
in:
```

In `advanced_freeq.py`

```git
-[default: ~/Documents/GitHubRepoes/advanced_freeq/mastered.csv ~/Documents/GitHubRepoes/advanced_freeq/COCA_top5000.csv]
+[default: <yourlocalRepositoryPath>/advanced_freeq/mastered.csv <yourlocalRepositoryPath>/advanced_freeq/COCA_top5000.csv]
```


## Thanks to

@[Enaunimes](https://github.com/Enaunimes/freeq); 12dicts word list: <http://wordlist.aspell.net/12dicts-readme/>

lemmas.txt is derrived from 2+2+3lem.txt in version 6 of 12dicts word
list.



