<h1 align="center">Embedding</h1>

#### [한국어](./Embedding(kor).md)

<h2 align="center">What is Embedding?</h2>

Computers cannot directly process natural language and its forms. Since computers can only perform numerical operations, natural language must be converted into numbers or vectors. This process is called embedding in the field of natural language processing. In other words, embedding refers to the process of numerically expressing a word or sentence in a vector space. Therefore, it is often used as an input value for other deep learning models.

Embeddings contain grammatical information because they vectorize according to a word. So, as long as the embedding quality is good, even a simple AI model can achieve great results.

Embedding can be divided into sentence embedding and word embedding.


<h2 align="center">Sentence Embedding?</h2>

Sentence embedding is a method of expressing individual words as vectors by grasping the flow of the entire sentence. So it has the advantage of having contextual meaning. For this reason, it is of better quality than word embeddings and is often used in commercial systems.

However, it requires a lot of sentence data to embed, and it costs a lot to learn.


<h2 align="center">Word Embedding?</h2>

Word embeddings are a way to represent individual words as vectors. Let's take the example of word embeddings.

> If there are only 3 words 'school', 'computer', and 'home' and 1, 2, 3 in that order, the word embedding is school (1,0,0), computer (0,1,0), Represents a house as (0,0,1) . This is called one-hot encoding. Each row of the word document matrix, the vector representing the document, is equal to the sum of all the word vectors that make up the document.

In the case of word embedding, since it does not distinguish between homonyms, even if the meanings are different, if the words have the same shape, they are expressed as the same vector value.

However, these word embeddings also have the advantage of being used in practice because the learning method is simpler compared to sentence embeddings.

<h2 align="center">What We Gonna Do?</h2>

Let's try word embedding that is often used in practice. Types of word embeddings include 'Word2Vec' as well as the above example 'One-Hot-Encoding'.
<h4>⚠️Each process uses the konlpy package!</h4>

 > [🔍 Find out what is a KoNLPy!](../Tokenizing/) <br>
 > [🔍 Find out what is a One-Hot Encoding!](./Word-Embedding/One-Hot-Encoding/One-Hot-Encoding(eng).md) <br>
 > [🔍 Find out what is a Word2Vec!](./Word-Embedding/Word2Vec/Word2Vec(eng).md) <br>
