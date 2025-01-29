import unittest
import calculadora

calc = calculadora

class testDivisionCajaBlanca(unittest.TestCase):

        def test_if(self):
                self.assertEqual(calc.division(4,2),2)
                self.assertEqual(calc.division(9,3),3)

        def test_else(self):
                self.assertEqual(calc.division(5,0), "Error, el dividendo debe ser mayor a 0")
                self.assertEqual(calc.division(3,-1), "Error, el dividendo debe ser mayor a 0")

if __name__ == '__main__':
    unittest.main()
