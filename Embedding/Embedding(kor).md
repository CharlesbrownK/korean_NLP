<h1 align="center">Embedding</h1>

<h2 align="center">What is Embedding?</h2>

컴퓨터는 자연어를 직접 그 형태를 처리할 수 없습니다. 컴퓨터는 수치 연산만 가능하기 때문에 자연어를 숫자나 벡터 형태로 변환해야 합니다. 이러한 과정을 자연어 처리 분야에서는 임베딩(Embedding)이라고 부릅니다. 즉, 임베딩(Embedding)은 단어나 문장을 수치화하여 벡터 공간으로 표현하는 과정을 의미합니다. 따라서 다른 딥러닝 모델의 입력값으로 많이 사용됩니다.

임베딩은 말뭉치(어절)에 따라 벡터화하기 때문에 문법적인 정보가 포함되어 있습니다. 따라서 임베딩 품질이 좋다면, 단순한 인공지능 모델로도 훌륭한 결과를 얻을 수 있습니다.

임베딩은 크게 문장 임베딩과 단어 임베딩으로 나눌 수 있습니다.


<h2 align="center">Sentence Embedding?</h2>

문장 임베딩은 전체 문장의 전체 문장의 흐름을 파악해 개별 단어를 벡터로 표현하는 방법입니다. 따라서 문맥적 의미를 지니다는 장점을 지닙니다. 이런 이유로 단어 임베딩 보다 품질이 좋으며, 상용 시스템에 많이 사용됩니다.

하지만, 임베딩하기 위해서 많은 문장 데이터가 필요하며 학습하는데 많은 비용이 들어갑니다.


<h2 align="center">Word Embedding?</h2>

단어 임베딩은 개별 단어를 벡터로 표현하는 방법입니다. 단어 임베딩의 예시를 들어보겠습니다.

> '학교', '컴퓨터', '집' 3단어만 있고 순서대로 1번, 2번, 3번이라면, 단어 임베딩은 학교를 (1,0,0), 컴퓨터를 (0,1,0), 집을 (0,0,1) 로 나타냅니다. 이를 one-hot encoding이라고 합니다. 단어 문서 행렬의 각 행, 즉 문서를 나타내는 벡터는 그 문서를 이루는 단어 벡터들을 모두 더한 것과 같습니다.

단어 임베딩의 경우, 동음이의어에 대한 구분을 하지 않기 때문에 의미가 다르더라도 단어의 형태가 같다면 동일한 벡터 값으로 표현되는 단점이 있습니다.

하지만, 이러한 단어 임베딩도 문장 임베딩에 비해 학습 방법이 간단해 여전히 실무에서 많이 사용한다는 장점아닌 장점이 있습니다.


<h2 align="center">What We Gonna Do?</h2>

우리는 실무에서 많이 사용되는 단어 임베딩을 해볼 것입니다. 단어 임베딩의 종류에는 위의 사례인 'One-Hot-Encoding' 뿐만 아니라 'Word2Vec' 등이 있습니다. 각각의 종류들을 예제 코드를 통해서 체험해 보도록 하겠습니다.(:caution: 각각의 과정들은 konlpy 패키지를 이용하고 있습니다.)
<h4>⚠️각각의 과정은 konlpy 패키지를 사용합니다!</h4>

 > [🔍 KoNLPy가 무엇인지 확인하러 가기!](../Tokenizing/) <br>
 > [🔍 One-Hot Encoding이 무엇인지 확인하러 가기!](./Word-Embedding/One-Hot-Encoding/) <br>
 > [🔍 Word2Vec이 무엇인지 확인하러 가기!](./Word-Embedding/Word2Vec/) <br>
