i = 0
s = [1,2,3,4]
t = [5,6,7,8]
while i < len(s) and i < len(t):
    x = s[i]
    y = t[i]
    print(x,y)
    i+=1

print()
#==

for x,y in zip(s,t):
    print(x,y)