# -*- coding:utf-8 -*-
"""
이터레이터를 활용한 range() 기능을 하는 함수 만들기
"""
class Counter:
    def __init__(self,stop):
        self.current = 0
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
    # def __iter__(self):
    #         return self
    #
    # def __next__(self):
    #     if self.current < self.stop:
    #         r = self.current
    #         self.current += 1
    #         return r
    #     else:
    #         raise StopIteration


print(Counter(3)[0],Counter(3)[1],Counter(3)[2])

for i in Counter(3):
    print(i,end=" ")

print()

# 언패킹도 가능함
a,b,c = Counter(3)
print(a,b,c)

