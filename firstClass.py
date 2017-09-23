arr = [5,2,3,4,2,4,5]

#      0,1,2,3,4,5,6
result = []
max_length = 0
max_value = 0

for i in range(len(arr)) :
     for j in range(0,len(arr)) :
         if arr[i]==arr[j] :
             if max_length < j - i :
                 max_length = j - i
                 max_value = arr[i]






print "max_length : {} \n max_value : {}" .format(max_length,max_value)

