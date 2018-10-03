# test
import unittest

class MulTest(unittest.TestCase): # unittest 대상.
	def test_simple(self):
		self.assertEqual(6, mul(2,3)) # 2*3 = 6
		self.assertEqual(6, mul(3,2))
		self.assertEqual(12, mul(4,3))
		
def mul(a, b):
	return 6

if __name__ == '__main__':
	unittest.main()