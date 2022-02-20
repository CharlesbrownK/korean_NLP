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
komoran = Komoran(userdic='./user_dic.tsv')

text = "나는 엔엘피를 좋아해!"

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(pos)
