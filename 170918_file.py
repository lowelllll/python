
# f = open("test.txt")
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()


# for line in open("test.txt"):
#     print(line)

f = open("test.txt","w")
print >> f, "%3s" %(" hi")
#f.write("%3s" %("hi"))
f.close()
#write





