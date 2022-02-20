<h1 align="center">Komoran</h1>

<h2 align="center">About Komoran</h2>

Komoran(Korean Morphological ANalyzer)은 Shineware에서 자바로 개발한 한국어 형태소 분석기입니다. '코모란'으로 발음하며, Apache 라이선스 2.0을 따르는 오픈소스 소프트웨어입니다.

KoNLPy의 코모란 형태소 분석기를 사용하기 위해서는 다음과 같이 konply 패키지를 설치해야 합니다.

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

설치가 완료되었다면,

```python
from konlpy.tag import Komoran
```

위의 코드를 입력하여 Komoran 모듈을 불러옵니다.

다음은 기본적인 Komoran 모듈의 함수 설명입니다.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|인자로 입력한 문장을 형태소 단위로 토크나이징합니다. 여기서 토크나이징이란, 주어진 장에서 토큰(Token) 단위로 정보를 나누는 작업입니다. 토크나이징된 형태소들은 리스트 형태로 반환됩니다.|
|nouns(phrase)|인자로 입력한 문장에서 품사가 명사인 토큰들만 추출합니다.|
|pos(phrase, flatten=True)|POS tagger라 부르고, 인자로 입력한 문장에서 형태소를 추출한 뒤 품사 태깅을 합니다. 추출된 형태소와 그 형태소의 품사가 튜플 형태로 묶여 리스트로 반환됩니다.|


<h2 align="center">Code</h2>
 > [🔍 코드 보러 가기!](./codes)


## Komoran Part of Speech Tags
Komoran은 총 42개의 품사 태그를 지원합니다. 하지만, 문장에 따라 정확한 형태소 분석이 안 될 수도 있습니다.
|품사|설명|
|:---:|:---:|
|NNG|일반 명사|
|JKS|주격 조사|
|JKB|부사격 조사|
|VV|동사|
|EF|종결 어미|
|SF|마침표, 물음표, 느낌표|


<h2 align="center">Build User Dictionary</h2>

 > [🔍 코드 보러 가기!](./codes/Komoran2.py)
위의 코드를 실행하면 아래의 결과가 나오는 것을 확인할 수 있습니다.

```
[('나', 'NP'), ('는', 'JX'), ('엔', 'NNB'), ('엘', 'NNP'), ('피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('!', 'SF')]
```

결과를 보면, 코모란이 '엔엘피'라는 단어를 '엔', '엘', '피' 문자로 분리해 명사로 인식했습니다. 단어의 토큰을 사용해 의미를 분석하는 코모란의 경우, 사용사 사전에 '엔엘피'라는 새로운 단어를 등록해야 합니다.

 > [🔍 사용자 정의 사전 보러 가기!](./codes/user_dic.tsv)

그러고 나서 다시 코드를 실행시켜 보면

```
[('나', 'NP'), ('는', 'JX'), ('엔엘피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('!', 'SF')]
```

라고 출력된 것을 확인할 수 있습니다.


<h2 align="center">Also..</h2>
만약 추가적인 정보를 원하시면, Komoran 웹사이트를 방문해주세요! <br>

 > [👉 Komoran 웹사이트로 가기](https://docs.komoran.kr/)
