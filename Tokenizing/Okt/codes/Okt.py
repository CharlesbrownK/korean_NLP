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

from konlpy.tag import Okt

# Okt 형태소 분석기 객체 생성
okt = Okt()

text = "어머니께서 방에 들어가십니다."

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출
text = "오늘 따라 왜인지 코딩이 그렇게 하고 싶더군욬ㅋㅋ"
print(okt.normalize(text))
print(okt.phrases(text))
