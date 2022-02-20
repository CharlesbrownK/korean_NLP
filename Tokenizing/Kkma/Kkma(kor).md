<h1 align="center">Kkma</h1>


<h2 align="center">About Kkma</h2>

Kkma는 서울대학교 IDS(Intelligent Data Systems) 연구실에서 자연어 처리를 위해 개발한 한국어 형태소 분석기입니다. Kkma는 '꼬꼬마'로 발음하며, GPL v2 라이선스를 따릅니다.

KoNLPy의 꼬꼬마 형태소 분석기를 사용하기 위해서는 다음과 같이 konply 패키지를 설치해야 합니다.

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
from konlpy.tag import Kkma
```

위의 코드를 입력하여 Kkam 모듈을 불러옵니다.

다음은 기본적인 Kkma 모듈의 함수 설명입니다.
|Function|Information|
|:---:|:---:|
|morphs(phrase)|인자로 입력한 문장을 형태소 단위로 토크나이징합니다. 여기서 토크나이징이란, 주어진 장에서 토큰(Token) 단위로 정보를 나누는 작업입니다. 토크나이징된 형태소들은 리스트 형태로 반환됩니다.|
|nouns(phrase)|인자로 입력한 문장에서 품사가 명사인 토큰들만 추출합니다.|
|pos(phrase, flatten=True)|POS tagger라 부르고, 인자로 입력한 문장에서 형태소를 추출한 뒤 품사 태깅을 합니다. 추출된 형태소와 그 형태소의 품사가 튜플 형태로 묶여 리스트로 반환됩니다.|
|sentences(phrase)|인자로 입력한 여러 문장을 분리해주는 역할을 합니다. 분리된 문장은 리스트 형태로 반환됩니다.|


<h2 align="center">Code</h2>

 > [🔍 코드 보러 가기!](./codes)


<h2 align="center">Kkma Part of Speech Tags</h2>

Kkma는 총 56개의 품사 태그를 지원합니다. 하지만, 문장에 따라 정확한 형태소 분석이 안 될 수도 있습니다.
|품사|설명|
|:---:|:---:|
|NNG|일반 명사|
|JKS|주격 조사|
|JKM|부사격 조사|
|VV|동사|
|EFN|평서형 종결 어미|
|SF|마침표, 물음표, 느낌표|


<h2 align="center">Also..</h2>

만약 추가적인 정보를 원하시면, Kkma 웹사이트를 방문해주세요!
 > [👉 Kkma 웹사이트로 가기](http://kkma.snu.ac.kr/)
