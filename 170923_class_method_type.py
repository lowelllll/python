# -*- coding: UTF-8 -*-
#클래스 객체와 인스턴스는 호출가능한 객체
class bar():
    def __init__(self):
        print "클래스 객체 호출"
    def __call__(self,args):
        print "인스턴스 객체 %d번 호출" %(args)

b = bar()
b(5)

class foo(object):
    a = 10
    pass
#object 클래스를 정의하면 타입이 type인 객체 생성
t = type(foo)
f = foo()
print type(foo)
print type(f)

print t.__dict__ #type객체 속성


