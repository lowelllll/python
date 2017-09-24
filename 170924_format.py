# -*- coding: UTF-8 -*-
#__format__() 실행
a = 42
b = 13.1231424
c = "hello"
d = {'x':13,'y':1.23142,'z':'world'}
e = 12313890730

def calc(r):
    print(r)

calc(r="a is %d" %a)
calc(r="%10d %f " %(a,b))
calc(r="%(x)d , %(y)f" %d)
calc(r="%*.*f" %(1,5,b))

stork = {
    'name':'yejin',
    'age':18,
    'weight':47.5
}

r="%(name)s, %(age)d , %(weight)0.2f" %stork
print(r)

#vars()가 호출된 시점에 정의되어있는 모든 변수를 담는 사전을 반환
name = "yejin"
age = 18

r = "%(name)s is %(age)d years old" % vars()
print(r)

#고급 포맷팅 format()

r = "{0} {1} {2}" .format('good',1,1.3) #일반 위치 인수 자리교체
r = "{name},{age},{height}".format(height=154.9,name="yejin",age=18) #키워드 인수
print(r)
r = "Hello {0}, {name}" .format(1,name="yejin" ) #위치,키워드인수
r = "this is dic {{ 0 }}" .format("dicc") #{{ -> {
print(r)

#dic을 활용한 고급 포맷팅
stork = {
    'name':'yejin',
    'age':18,
    'weight':47.5
}

r = "{0[weight]} , {0[name]} , {0[age]}" .format(stork)
# 0 = stork , stork['weight']
print(r)

# x = -1
# r = "{abs(0)}".format(x)
# print(r)



print("*{0:-^30}*".format("start"))
#{0:<10} 왼쪽정렬
#{0:>10} 오른쪽정렬
#{0:^10} 중앙정렬

x = 42
print("{0:010b}".format(x)) #앞쪽의 빈공간이 0으로 채워짐
# b 2진수

y = 3.141592
print("{0:{width}.{p}f}".format(y,width=10,p=3))
print("%6.3f" %(y)) #6 총길이 3 소숫점