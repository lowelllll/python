def print_find(find):
    print "looking for",find
    while True:
        line = (yield)

        if find in line:
            print line


f = print_find("yejin")
f.next()
f.send("python")
f.send("yejin is amazing")
f.close()