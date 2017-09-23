def count(n):
    print "counting Down!"
    while n > 0:
        yield n

        n -= 1;

#
# c = count(5)
# c.next()
# c.next()

for i in count(5):
    print i
