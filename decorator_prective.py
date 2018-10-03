def base_10(func):
	base_num = 10;
	def wrap(x,y):
		return func(x,y)+base_num
	return wrap

def base(base_num):
	def inner_base(func):
		def wrap(x,y):
			return func(x,y)+base_num
		return wrap
	return inner_base

def mysum(x,y):
	return x+y


yoursum = base_10(mysum) # 같음
print(yoursum(1,2))

@base_10 # 같음.
def hissum(x,y):
	return x+y

print(hissum(1,2)) 