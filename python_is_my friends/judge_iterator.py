# -*- coding : utf-8 -*-
"""
iterator를 만들어 시간 이터레이터를 만듬
"""
class TimeIterator:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        self.current = self.start

    def __getitem__(self, index): # 인덱스 요청시
        index = self.start + index
        if  index < self.stop:
            hour = index // 3600 % 24
            minuit = index // 60 % 60
            second = index % 60

            return "{0:02d}:{1:02d}:{2:02d}".format(hour, minuit, second)
        else:
            raise IndexError

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            hour = self.current // 3600 % 24
            minuit = self.current // 60 % 60
            second = self.current % 60

            self.current += 1
            return "{0:02d}:{1:02d}:{2:02d}".format(hour,minuit,second) # 00:00:00 식으로 나옴
        else:
            raise StopIteration



start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')