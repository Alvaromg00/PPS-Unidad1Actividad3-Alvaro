import unittest
import calculadora

calc = calculadora

class testMultiplicacionCajaBlanca(unittest.TestCase):

        def test_multiplicacion(self):
                self.assertEqual(calc.multiplicacion(5,3),15)
                self.assertEqual(calc.multiplicacion(2,3.5),7)

if __name__ == '__main__':
    unittest.main()
