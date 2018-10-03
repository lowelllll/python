import unittest

class SumTest(unittest.TestCase):
	# def test_sum(self):
	# 	result = summary(6, '1 2 3 4 10 11')
	# 	self.assertEqual(result, 31)

	def test_sum_raise_exception(self):
		self.assertRaises(Exception, lambda: summary(5, '1 2 3 4 10 11')) # excpetion이 발생하냐?

def summary(size, data):
	numbers = [int(num) for num in data.split(' ')]
	if size!= len(numbers):
		raise Exception('array size is not matched')
	return sum(numbers)

if __name__ == '__main__':
	unittest.main()
