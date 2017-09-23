# -*- coding: UTF-8 -*-
#not deep
a = [1,2,[3,4]]
b = list(a) #얕은복사
print b is a
b.append(100) #새로생성된 객체 b에 새로운 원소는 a에 적용x
print b
print a
b[2][0]=-100#공유하는 원소에 변화를 가하면 a에 적용o
b[3]=200
print b
print a

print id(b)
print id(a)

print "------------------------"

import copy

a = [1,2,[3,4]] #깊은복사
b = copy.deepcopy(a)
b[2][0]=-100

print b
print a

print "------------------------"
a1 = [1,2,3,4]
a2 = a1

print id(a1)
print id(a2) #참조
