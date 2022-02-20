<h1 align="center">Okt</h1>

<h2 align="center">About Okt</h2>

Okt(Open-source Korean Text Processor)는 트위터에서 개발한 Twitter 한국어 처리기에서 파생된 오픈소스(Apache 라이선스 2.0) 한국어 처리기입니다.
공식 홈페이지에 따르면 Okt는 빅데이터에서 간단한 한국어 처리를 통해 색인어를 추출하는 목적을 갖고 있기 때문에 완전한 수준의 형태소 분석을 지향하지는 않습니다.
따라서 공식적으로는 Okt를 한국어 처리기라고 표현하고 있습니다. Okt는 띄어쓰기가 어느정도 되어 있는 문장을 빠르게 분석할 때 많이 사용합니다.

KoNLPy의 Okt 한국어 처리기를 사용하기 위해서는 다음과 같이 konply 패키지를 설치해야 합니다.

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

설치가 완료되었다면,

```python
from konlpy.tag import Okt
```

위의 코드를 입력하여 Okt 모듈을 불러옵니다.

다음은 기본적인 Okt 모듈의 함수 설명입니다.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|인자로 입력한 문장을 형태소 단위로 토크나이징합니다. 여기서 토크나이징이란, 주어진 장에서 토큰(Token) 단위로 정보를 나누는 작업입니다. 토크나이징된 형태소들은 리스트 형태로 반환됩니다.|
|nouns(phrase)|인자로 입력한 문장에서 품사가 명사인 토큰들만 추출합니다.|
|pos(phrase, flatten=True, join=False)|POS tagger라 부르고, 인자로 입력한 문장에서 형태소를 추출한 뒤 품사 태깅을 합니다. 추출된 형태소와 그 형태소의 품사가 튜플 형태로 묶여 리스트로 반환됩니다.|
|normalize(phrase)|입력한 문장을 정규화시킵니다. ex) 사랑햌ㅋ --> 사랑해ㅋ|
|phrases(phrase)|입력한 문장에서 어구를 추출합니다. ex) 입력 : 오늘 날씨가 좋아요 / 출력 : ['오늘','오늘 날씨','날씨']|


<h2 align="center">Code</h2>

 > [🔍 코드 보러 가기!](./codes)


<h2 align="center">Okt Part of Speech Tags</h2>

|품사|설명|
|:---:|:---:|
|Noun|명사|
|Verb|동사|
|Adjective|형용사|
|Josa|조사|
|Punctuation|구두점|


<h2 align="center">Also..</h2>

만약 추가적인 정보를 원하시면, 깃허브의 Okt 레포를 방문해주세요! <br>
 > [👉 Okt 레포로 가기](https://github.com/open-korean-text/open-korean-text)
