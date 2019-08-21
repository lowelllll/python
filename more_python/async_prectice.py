import asyncio

async def hello():
	"""
	네이티브 코루틴
	"""
	print('hello world')


async def add(a, b):
	print(f'add : {a} + {b}')
	await asyncio.sleep(1.0) 
	return a + b


async def print_add(a, b):
	result = await add(a, b)
	print(f'print_add :{a} + {b} = {result}')


loop = asyncio.get_event_loop() # 이벤트 루프
loop.run_until_complete(print_add(1,2)) # hello가 끝날때 까지 기다림
# 네이티브 코루틴을 호출하면 코루틴 객체가 생성됨
# run_until_complete 에 코루틴 객체를 넣음.
loop.close()


