
s = [100,200,300]

i = 0
for n in s:
    print(i,n,end=" ")
    i+=1

#==
print()
for i,j in enumerate(s): #return index,value = (0,s[0])
    print(i,j,end=" ")
