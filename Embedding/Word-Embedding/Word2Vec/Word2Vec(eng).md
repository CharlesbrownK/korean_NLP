<h1 align="center">Word2Vec</h1>

#### [한국어](./Word2Vec(kor).md)


This article starts with the assumption that you know what Ont-Hot Encoding is.

 > [🔍 Let's Figure out what is One-Hot-Encoding!](../One-Hot-Encoding/One-Hot-Encoding(kor).md)

The one-hot encoding introduced earlier has the advantage of being simple to implement. However, in the case of artificial intelligence, the one-hot encoding technique may not be a good choice because it has to be able to calculate the similarity between words while processing many words to achieve good performance. Therefore, we will use a word embedding model in the form of a distributed representation. This time, we will look at the representative Word2Vec model among the neural network-based word embedding methods.


<h2 align="center">What is Word2Vec</h2>

**Word2Vec** was released by Google in 2013 and is the most used word embedding model. There is not much difference in structure compared to the existing neural network-based word embedding model, but it enables fast learning by surprisingly reducing the amount of computation. The Word2Vec model can be divided into two models: continuous bag-of-words (CBOW) and skip-gran.

First of all, you need to download the Word2Vec package.

### Ubuntu

```
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ python3 get-pip.py --user
$ pip install gensim
```

### Mac OS

```
$ pip3 install gensim
```

### Window

```
> pip install --upgrade pip
> pip install gensim
```


<h2 align="center">CBOW and skip-gram</h2>

Let's analyze the two models of Word2Vec described above, CBOW and skip-gram.

### CBOW

The CBOW model is a neural network model that predicts a target word using surrounding words expressed as context. We use the learned weight data as an embedding vector by composing the input of the neural network with surrounding words and setting the output as the target word. The CBOW model has the advantage of fast learning because it only needs to calculate the disappearance of the target word.

### skip-gram

The skip-gram model is a neural network model that predicts surrounding words using a single target word as opposed to the CBOW model. Because the input and output are inversed to the CBOW model, the skip-gram model has more context to predict compared to the CBOW model. As a result, the word dispersion expression is excellent and the embedding quality is superior to that of the CBOW model.


<h2 align="center">Word2Vec Model</h2>

You can implement the Word2Vec model yourself using a neural network library such as TensorFlow or Keras, but an open source library already exists and the embedding quality is not bad, so we will use the popular **Genism** package.

To create a Korean Word2Vec, you need to collect a Korean corpus. In this example, we will create a model using <strong>Naver Sentiment Movie Corpus (NSMC)</strong>. The [rating.txt](./codes/ratings.txt) that I will use may be outdated, so if you want the latest version of the football data, please refer to [New-rating.txt](https://github.com/e9t/nsmc) ) can be downloaded from

The corpus data is large and it takes some time to train the model. Since we can't do the lengthy model training every time we use Word2Vec, we will save the model with the embedding vectors for each word set to a file.

 > It took me 254s to learn the rating.txt(19MB) file with Word2Vec. The learning time may vary depending on the computer specifications of the viewers, so if you have a cup of ☕ (coffee) in your spare time, a model file will be created.

After the model training is complete, enter a code like [laod_word2vec_model.py](./codes/nvmc-model/laod_word2vec_model.py) to check the actual word embedded value and similar words in the vector space.

If you write the code and run it:

```
corpus_total_words :  1076896
달력 :  [ 9.32990983e-02 -1.34993032e-01 -1.03150487e-01  4.69429232e-02
 -3.20427082e-02  8.99038613e-02  5.08054346e-02  3.48317266e-01
 -1.52057752e-01  1.65496647e-01 -9.49010924e-02 -4.26943362e-01
    ......
  3.09792638e-01 -1.64287269e-01 -3.22148092e-02 -1.22924365e-01
 -1.61299482e-01 -1.79409847e-01  1.38744682e-01  5.65950647e-02]
일요일 = 월요일  0.64878
안성기 = 배우    0.59924126
대기업 = 삼성    0.4369776
일요일 != 삼성   0.27672067
히어로 != 삼성   0.20656006
[('씨야', 0.7492166757583618), ('정려원', 0.7250934839248657), ('김유미', 0.7148603200912476), ('정재영', 0.7102662920951843), ('김흥국', 0.7097449898719788)]
[('더 울버린', 0.664757490158081), ('엑스맨', 0.6643115878105164), ('캐리비안의 해적', 0.6600803732872009), ('편', 0.6376581788063049), ('X맨', 0.6375453472137451)]
```

You can see that the same result is displayed.

 > When training the model, the initial weight of each node in the neural network is set at random. Therefore, each time the model is trained, the embedding vector value of the word changes. Therefore, when comparing results, they may differ from mine.

If you try to check similarity by typing another word, it sometimes finds surprisingly similar words, but sometimes it outputs results that are difficult to understand. This is a phenomenon that occurs because there is not enough corpus data for a topic, so learning good-quality corpus data improves embedding performance.


<h2 align="center">Further</h2>

Let's write code that simply uses the input built-in function to find similar words.

 > [🔍 Let's figure out the code!](./codes/nvmc-model/find-similar-word.py)

In my case, I typed in 'Wolverine' in korean and ordered it to find 8 similar words.

```
Enter any word that you want to find similar word : 울버린
How many similar words you want? : 8
[('고지라', 0.6919588446617126), ('퍼스트 클래스', 0.6855024099349976), ('X맨', 0.6837846636772156), ('엑스맨', 0.6686899662017822), ('착신아리', 0.6667824983596802), ('스코어', 0.6567636728286743), ('러브 액츄얼리', 0.6380522847175598), ('왜놈', 0.6359009742736816)]
```

So the result is as above.


<h2 align="center">Finally</h2>

If the quality of the corpus and the amount of data are sufficient, a high-quality embedding model can be built. This embedding is commonly used as an input for neural network models because it converts information that a human understands into a form that a computer can understand.
