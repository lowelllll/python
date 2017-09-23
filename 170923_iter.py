list = [1,2,3,4,5]

_iter = list.__iter__()
while 1:
    try:
        x = _iter.next() #python 3 __next__()
        print x
    except StopIteration:
        break

# for i in list:
    #print i