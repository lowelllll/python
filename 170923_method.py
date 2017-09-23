# -*- coding: UTF-8 -*-
class foo():
    def instance_method(self,arg):
            print self,arg
    def class_method(cls,arg):
            print cls,arg
    def static_method(arg):
            print arg


f = foo();
f.instance_method(1235) #types.MethodType
f.class_method(1234)  #types.MethodType

#f.static_method(1233)

b = foo()
meth = b.instance_method #bound method 함수와 연관된 인스턴스를 감싸는 호출가능 객체
meth(37)

umeth = foo.instance_method #unbound method 클래스 자체로 메서드검색
umeth(f,100) #인스턴스(self)를 직접 전달  호출가능객체

