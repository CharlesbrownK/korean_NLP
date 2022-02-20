<h1 align="center">Kkma</h1>

#### [한국어](./Kkma(kor).md)

<h2 align="center">About Kkma</h2>

Kkma is a Korean morpheme analyzer developed for natural language processing in the Intelligent Data Systems (IDS) laboratory of Seoul National University. Kkma is licensed under the GPL v2.

To use KoNLPy's Kkma stemmer, you need to install the konply package as follows:

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
from konlpy.tag import Kkma
```

Enter the code above to load the Kkam module.

The following is a description of the functions of the basic Kkma module.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|Tokenizes the sentence input as an argument in units of morphemes. Tokenizing here is the operation of dividing information into token units in a given chapter. Tokenized morphemes are returned in the form of a list.|
|nouns(phrase)|Only tokens whose part-of-speech is a noun are extracted from the sentence input as an argument.|
|pos(phrase, flatten=True)|It is called POS tagger, and after extracting morphemes from the sentences input as arguments, tagging is done. The extracted morpheme and the part-of-speech of the morpheme are grouped in a tuple form and returned as a list.|
|sentences(phrase)|It serves to separate multiple sentences entered as arguments. Separated statements are returned in the form of a list.|


<h2 align="center">Code</h2>

 > [🔍 Find out the Code!](./codes)


<h2 align="center">Kkma Part of Speech Tags</h2>

Kkma supports a total of 56 parts-of-speech tags. However, depending on the sentence, the correct morphological analysis may not be possible.
|Parts-of-speech|Explanation|
|:---:|:---:|
|NNG|Common Noun|
|JKS|Prepositional particle for nominative|
|JKM|Prepositional particle for adverb|
|VV|Verb|
|EFN|Sentence-closing ending|
|SF|Period, Question mark, Exclamation point|


<h2 align="center">Also..</h2>

If you want more information, Please go to the 'Kkma' website!
 > [👉 Go to the Kkma](http://kkma.snu.ac.kr/)
