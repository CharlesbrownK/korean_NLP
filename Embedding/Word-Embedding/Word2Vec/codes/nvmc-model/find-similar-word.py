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

from gensim.models import Word2Vec

# Code Model
model = Word2Vec.load('/home/charlesbrownk/바탕화면/Pythonic/Ai_Chatbot/Hey-bugo/Embedding/Word-Embedding/Word2Vec/codes/nvmc-model/nvmc.model') # This is my absolute path so you have to change your directory

# get words that user enters
word = input('Enter any word that you want to find similar word : ')
how_many = int(input('How many similar words you want? : '))

# Extract the most Similar Words
print(model.wv.most_similar(word, topn=how_many))
