# -*- coding:utf-8 -*-
"""
회문을 판단하는 프로그램
ex)level->회문 hello -> not 회문
"""
class NotPalindromeError(Exception): # 회문이 아닐시 일으킬 exception 생성
    def __init__(self):
        super(NotPalindromeError, self).__init__('회문이 아닙니다')

def palindrome(word):
    if len(word) == 1:
        raise NotPalindromeError
    harfWord = int(len(word)/2)
    # print(harfWord)
    for i in range(harfWord):
        if word[i] == word[-(i+1)]:
            pass
        else:
            raise NotPalindromeError

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
else:
    print('회문입니다')



