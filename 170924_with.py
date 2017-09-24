# -*- coding: UTF-8 -*-
with open("0924.txt","r") as f:
    line = f.readline()
# with 블록을 벗어날때 열린파일을 자동으로 닫음

#컨텍스트 관리 (프로토콜)

class ListTransaction(object):
    def __init__(self,thelist):
        self.thelist = thelist
    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.thelist[:] =  self.workingcopy
            return False

#리스트에 일련의 변경을 가할수 있는 기능 예외가 발생하지 않은 경우
# 예외가 발생하면 리스트는 변경이 안됨

items = [1,2,3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
print(items)

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("we re hosed")
except RuntimeError:
    pass
print(items) #변경안됨.

