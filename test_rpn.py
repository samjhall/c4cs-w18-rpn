import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_Add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_div(self):
		result = rpn.calculate('6 4 /')
		self.assertEqual(1.5, result)
	def test_mul(self):
		result = rpn.calculate('2 2 *')
		self.assertEqual(4, result)
	def test_percent(self):
		result = rpn.calculate('72 5 %')
		self.assertEqual(75.6, result)
	def test_exponent(self):
		result = rpn.calculate('2 2 ^')
		self.assertEqual(4, result)
	def test_intDiv(self):
		result = rpn.calculate('5 2 .')
		self.assertEqual(2, result)
#	def test_sum(self):
#		result = rpn.calculate('1 2 3 4 5 S')
#		self.assertEqual(15, result)
#	def test_copy(self):
#		result = rpn.calculate('1 2 3 C S')
#		self.assertEqual(9, result)
