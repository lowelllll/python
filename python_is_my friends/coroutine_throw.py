# -*- coding : utf-8 -*-
def sum_coroutime(): # 코루틴
    try:
        total  = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total

co = sum_coroutime() # 코루틴 객체 생성
next(co) # 최초 실행

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError,'예외로 코루틴 끝내기'))
# throw 예외를 던짐
# 코루틴의 except에서 yield로 전달받은 값 반환
