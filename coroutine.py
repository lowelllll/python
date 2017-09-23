# -*- coding: UTF-8 -*-
def print_find(find):
    print "looking for",find
    while True:
        line = (yield)
        if find in line:
            print line

c = print_find("파이썬")
c.next()
c.send("파이썬이양")