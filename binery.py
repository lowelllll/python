
list = [2,4,6,8,10,12,14,16,18,20]
min = 0
max = len(list)-1
mid = 0
number = int(raw_input("Enter Number:"))

print "finding {}....." .format(number)

while True:

    if max-min == 1:
         print "find!! index :" ,max
         break

    mid = (min+max)/2

    if list[mid] > number :
        max = mid
        print "{} > {},max:{},min:{}".format(list[mid], number,list[max],list[min])

    elif list[mid] < number :
        min = mid
        print "{} < {},max:{},min:{}".format(list[mid], number,list[max],list[min])

    elif list[mid] == number :
        print "find!! index :",mid
        break

