# -*- coding:utf-8 -*-
"""
클래스로 매개변수가 있는 데코레이션 만들기
"""
class IsMultiple:
    def __init__(self,x):
        self.x = x

    def __call__(self, func): # 데코레이터를 만들기 위해 구현해야함
        def wrapper(a,b): # 매개변수가 없을 시에는 init에서 함수를 받음
            r = func(a,b)
            if r % self.x == 0:
                print("{}의 반환 값은 {}의 배수입니다".format(func.__name__,self.x))
            else:
                print("{}의 반환 값은 {}의 배수가 아닙니다".format(func.__name__,self.x))
            return r
        return wrapper


@IsMultiple(3)
def add(a,b):
    return a+b

print(add(10,20))