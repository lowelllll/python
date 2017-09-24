# -*- coding: UTF-8 -*-
a = [i for i in range(10)]

a[1] = 6
print(a)
a[2:4] = [10,11] #대입
print(a)
a[3:4] = [1,2,3,4]
print(a)
a[:] = [7,8]
print(a)
