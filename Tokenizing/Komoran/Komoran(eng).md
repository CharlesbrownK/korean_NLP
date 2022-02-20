<h1 align="center">Komoran</h1>

#### [한국어](./Komoran(kor).md)

<h2 align="center">About Komoran</h2>

Komoran (Korean Morphological ANalyzer) is a Korean morphological analyzer developed in Java by Shineware. Pronounced 'Kormoran', it is open-source software under the Apache License 2.0.

To use KoNLPy's Komoran stemmer, you need to install the konply package as follows.

### Ubuntu

```
$ sudo apt-get install g++ openjdk-7-jdk
$ sudo apt-get install python3-dev; pip3 install konlpy
```

### Mac OS

```
$ pip3 install konlp
```

### Window

```
> pip install --upgrade pip
> pip install konlpy
```


<h2 align="center">konlpy.tag</h2>

If install is completed,

```python
from konlpy.tag import Komoran
```

Enter the code above to load the Komoran module.

The following is a description of the functions of the basic Komoran module.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|Tokenizes the sentence input as an argument in units of morphemes. Tokenizing here is the operation of dividing information into token units in a given chapter. Tokenized morphemes are returned in the form of a list.|
|nouns(phrase)|Only tokens whose part-of-speech is a noun are extracted from the sentence input as an argument.|
|pos(phrase, flatten=True)|It is called POS tagger, and after extracting morphemes from the sentences input as arguments, tagging is done. The extracted morpheme and the part-of-speech of the morpheme are grouped in a tuple form and returned as a list.|


<h2 align="center">Code</h2>

 > [🔍 Find out the Code!](./codes/)


<h2 align="center">Komoran Part of Speech Tags</h2>

Komoran supports a total of 42 part-of-speech tags. However, depending on the sentence, the correct morphological analysis may not be possible.
|Part-of-speech|Explanation|
|:---:|:---:|
|NNG|Common Noun|
|JKS|Prepositional particle for nominative|
|JKB|Prepositional particle for adverb|
|VV|Verb|
|EF|Sentence-closing ending|
|SF|Period, Question mark, Exclamation point|


<h2 align="center">Build User Dictionary</h2>

 > [🔍 Find out the Code!](./codes/Komoran2.py)

If you run the above code, you can see the result below.

```
[('나', 'NP'), ('는', 'JX'), ('엔', 'NNB'), ('엘', 'NNP'), ('피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('!', 'SF')]
```

Looking at the results, Komoran recognized the word 'NLP' as a noun by separating it into 'N', 'L', and 'Pi' characters. In the case of Komoran, which analyzes meaning using tokens of words, a new word 'NLP' must be registered in the dictionary of users.

 > [🔍 Find out User Dictionary!](./user_dic.tsv)

Then run the code again

```
[('나', 'NP'), ('는', 'JX'), ('엔엘피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('!', 'SF')]
```

You can see what is printed out.


<h2 align="center">Also..</h2>

If you want more informations, Please go to the Komoran Website! <br>
 > [👉 Go to the Komoran site](https://docs.komoran.kr/)
