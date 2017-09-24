# -*- coding: UTF-8 -*-
#currying 함수인자들을 부분적으로 평가하는 것
#partial 함수의 인수들 중 일부분을 평가하고
# 나중에 나머지인수들을 제공해 호출할 수 있는 객체반환
from functools  import partial
def foo(x,y,z):
    return x+y+z

f = partial(foo,1,2) #foo 함수에 x,y 인자 고정(저장?)
result = f(3) #마지막 인자 제공
print(result)