# -*- coding:utf-8 -*-
"""
매개변수가 있는 decorator
"""
import functools

def is_multple(x):
    def real_decorator(func):
        @functools.wraps(func) # 함수의 이름 (func)의 이름을 출력하기 위해 지정
        # 원래의 함수의 정보를 유지해줌
        def wrapper(a,b):
            r = func(a,b)
            if r % x == 0:
                print("{}의 반환값은 {}의 배수입니다".format(func.__name__,x))
            else:
                print("{}의 반환 값은 {}의 배수가 아닙니다".format(func.__name__,x))
            return r
        return wrapper
    return real_decorator

@is_multple(5)
def add(a,b):
    return a+b

add(10,20)