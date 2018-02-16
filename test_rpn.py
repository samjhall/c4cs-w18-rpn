import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_Add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
