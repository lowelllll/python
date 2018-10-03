# generator fibonacci

def fib():
	x, y = 1, 1
	while True:
		yield x
		x , y = y , x+y 

fibo = fib()

# 소비하는 만큼 생산.
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))