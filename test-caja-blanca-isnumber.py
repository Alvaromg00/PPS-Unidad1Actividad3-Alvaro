import unittest
import calculadora

calc = calculadora

class testIsNumberCajaBlanca(unittest.TestCase):

	def test_try(self):
		self.assertTrue(calc.isNumber(2))
		self.assertTrue(calc.isNumber(4))

	def test_except(self):
		self.assertFalse(calc.isNumber("1,12"))
		self.assertFalse(calc.isNumber("-3,4"))

if __name__ == '__main__':
    unittest.main()
