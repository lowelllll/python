# -*- coding: UTF-8 -*-
class Exm(object):
    def __getitem__(self,index):
        print(index)

e = Exm()
e[3,...,4] #__getitem__ ((3,Ellipsis,4)) 색인연산자 호출