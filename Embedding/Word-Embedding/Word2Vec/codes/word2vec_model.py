#   Copyright (C) 2022 Junghoon Kim
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>

from asyncore import read
from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# Define Read Naver Movies' Reviews datas Function
def read_review_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    
    return data

# Start to Measure Learning Time
start = time.time()

# Read Reviews file
print('1) Start to read corpus data')
review_data = read_review_data('/home/charlesbrownk/바탕화면/Pythonic/Ai_Chatbot/Hey-bugo/Embedding/Word-Embedding/Word2Vec/codes/ratings.txt') # This is my absolute path so you have to change your directory
print(len(review_data)) # All number of review datas
print('1) Complete to read corpus data : ', time.time() - start)

# Extract only Nouns in Sentence Units and Make Them as Learning Input Data
print('2) Start extracting only nouns from morphemes')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) Complete extracting only nouns from morphemes : ', time.time() - start)

# Word2Vec Model Learning
print('3) Start learning Word2Vec model')
model = Word2Vec(sentences=docs, vector_size=200, window=4, hs=1, min_count=2, sg=1)
print('3) Complete learning Word2Vec model : ', time.time() - start)

# Save the Model
print('4) Start saving the trained model')
model.save('nvmc.model')
print('4) Complete saving the trained model : ', time.time() - start)

# Number of learned corpus, total number of words in the corpus
print('corpus_count : ', model.corpus_count)
print('corpus_total_words : ', model.corpus_total_words)
