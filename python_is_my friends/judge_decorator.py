# -*- coding:utf-8 -*-
"""
html 태그로 래핑하는 데코레이터
"""
# 함수 데코레이터
def html_tag(tag):
    def real_decorator(func):
        def wrapper():
            code = "<{}>".format(tag)
            code += func()
            code += "</{}>".format(tag)
            return code
        return wrapper
    return real_decorator

# 클래스 데코레이터
class HtmlTag:
    def __init__(self,tag):
        self.tag = tag
    def __call__(self, func):
        def wrapper():
            code = "<{}>".format(self.tag)
            code += func()
            code += "</{}>".format(self.tag)
            return code
        return wrapper



a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

@HtmlTag(a)
@HtmlTag(b)
def bye():
    return 'bye'

print(hello())
print(bye())