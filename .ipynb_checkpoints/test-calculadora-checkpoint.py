import unittest
import calculadora

calc = calculadora

class testIsNumberCajaNegra(unittest.TestCase):

    def test_integer(self):
        self.assertTrue(calc.isNumber(1))
        self.assertTrue(calc.isNumber(-1))
        self.assertTrue(calc.isNumber(0))
        self.assertTrue(calc.isNumber(3))
        
    def test_great_integer(self):
        self.assertTrue(calc.isNumber(9999999999999999999999999999999999999999999999999999999))

    def test_float(self):
        self.assertTrue(calc.isNumber(1.5))
        self.assertTrue(calc.isNumber(-1.5))
        self.assertTrue(calc.isNumber(-0))
        self.assertTrue(calc.isNumber(0.00000000000000000000000000000000000000001))

    def test_string_number(self):
        self.assertTrue(calc.isNumber("2.5"))
        self.assertTrue(calc.isNumber("2"))
        self.assertTrue(calc.isNumber("0"))

    def test_string_non_number(self):
        self.assertFalse(calc.isNumber("hola mundo"))
        self.assertTrue(calc.isNumber(""))

    def test_none(self):
        self.assertFalse(calc.isNumber(None))

    def test_boolean(self):
        self.assertTrue(calc.isNumber(True))
        self.assertTrue(calc.isNumber(False))

if __name__ == '__main__':
    unittest.main()
