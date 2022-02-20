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

from konlpy.tag import Komoran

# 코모란 형태소 분석기 객체 생성
komoran = Komoran()

text = "어머니께서 방에 들어가신다."

# 형태소 추출
morphs = komoran.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(pos)

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
