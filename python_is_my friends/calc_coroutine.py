# -*- coding:utf-8 -*-
"""
사칙연산 코루틴
"""
def calc(): # 코루틴
    result = 0
    while True:
        exp = (yield result)
        if '+' in exp:
            exp = exp.split('+')
            result = int(exp[0])+int(exp[1])
        elif '-' in exp:
            exp = exp.split('-')
            result = int(exp[0])-int(exp[1])
        elif '*' in exp:
            exp = exp.split('*')
            result = int(exp[0])*int(exp[1])
        elif '/' in exp:
            exp = exp.split("/")
            result = int(exp[0])/int(exp[1])
        else:
            result = "오류"

expressions = input().split(', ')

c = calc()
print(next(c)) # 최초실행 result의 초기값인 0을 받음


for e in expressions:
    print(c.send(e)) # result에 exp를 보내고 result를 받음

c.close()
