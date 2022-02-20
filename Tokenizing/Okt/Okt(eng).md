<h1 align="center">Okt</h1>

#### [한국어](./Okt(kor).md)

<h2 align="center">About Okt</h2>

Okt (Open-source Korean Text Processor) is an open-source (Apache license 2.0) Korean language processor derived from the Twitter Korean language processor developed by Twitter.
According to the official website, Okt is not oriented toward complete morphological analysis because the purpose of Okt is to extract index words from big data through simple Korean processing. Therefore, we are officially expressing Okt as a Korean processor. Okt is often used to quickly analyze sentences with some spacing.

To use KoNLPy's Okt Korean handler, you need to install the konply package as follows:

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


<h2 align="center">okt.tag</h2>

If install is completed,

```python
from konlpy.tag import Okt
```

Enter the code above to load the Okt module.

The following is a description of the functions of the basic Okt module.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|Tokenizes the sentence input as an argument in units of morphemes. Tokenizing here is the operation of dividing information into token units in a given chapter. Tokenized morphemes are returned in the form of a list.|
|nouns(phrase)|Only tokens whose part-of-speech is a noun are extracted from the sentence input as an argument.|
|pos(phrase, flatten=True, join=False)|It is called POS tagger, and after extracting morphemes from the sentences input as arguments, tagging is done. The extracted morpheme and the part-of-speech of the morpheme are grouped in a tuple form and returned as a list.|
|normalize(phrase)|Normalizes the entered sentence. ex) 사랑햌ㅋ --> 사랑해ㅋ|
|phrases(phrase)|Extracts phrases from the entered sentences. ex) 입력 : 오늘 날씨가 좋아요. / 출력 : ['오늘','오늘 날씨','날씨']|


<h2 align="center">Code</h2>

 > [🔍 Find out the Code!](./codes)


<h2 align="center">Okt Part of Speech Tags</h2>

|Part-of-speech|Explanations|
|:---:|:---:|
|Noun|Noun|
|Verb|Verb|
|Adjective|Adjective|
|Josa|Prepositional particles|
|Punctuation|Punctuation|


<h2 align="center">Also..</h2>

If you want more informations, Please go to the Okt github repo!
 > [👉 Go to the Okt repo](https://github.com/open-korean-text/open-korean-text)
