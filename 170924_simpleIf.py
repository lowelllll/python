# -*- coding: UTF-8 -*-
a = 10
b = 20

# if a <= b :
#     min = a
# else:
#     min = b

min = a if a<=b else b #조건표현식 조건이 가장먼저 평가됨.
#가급적 쓰지 x 리스트 내포에서 사용됨.
print(min)