# range, myrange

def myrange(start=0, end=0, step=1):
	mylist = []
	while start < end:
		mylist.append(start)
		start += step
	return mylist


def myxrange(start=0, end=0, step=1): # cotutine
	while start < end:
		yield start # generator 
		start += step

if __name__ == "__main__":
	for i in myrange(end=10):
		print(i)

	for i in myxrange(end=10):
		print(i)
