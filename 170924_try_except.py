# -*- coding: UTF-8 -*-
# a = int(input())
# b = input()
# try:
#     a+b
# except TypeError as e:
#     print("타입이 같아야 더할 수 있어용 ㅎㅎ %s" %e)
# else: #try 블록에서 예외가 발생하지 않은 경우
#     print("더하기 완료")
# finally: #예외발생유무에 상관없이 실행됨.
#     print("끝")

#새로운 예외 정의

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

def error1():
    raise HostnameError("HostnameError")

try:
    error1()
except NetworkError as e:
    if type(e) is HostnameError:
        print("NetworkError")