import unittest
import calculadora

calc = calculadora

class testDivisionCajaNegra(unittest.TestCase):

    def test_division_normal(self):
        self.assertEqual(calc.division(10, 2), 5)
        self.assertEqual(calc.division(9, 3), 3)
        self.assertEqual(calc.division(-10, 2), -5)
        self.assertEqual(calc.division(10, -2), -5)
        self.assertEqual(calc.division(-10, -2), 5)

    def test_division_decimal(self):
        self.assertAlmostEqual(calc.division(10, 3), 10 / 3)  # Resultado aproximado
        self.assertAlmostEqual(calc.division(1.5, 0.5), 3.0)

    def test_division_divisor_cero(self):
        self.assertEqual(calc.division(10, 0), "Error: División por cero")

    def test_division_dividendo_cero(self):
        self.assertEqual(calc.division(0, 10), 0)
        self.assertEqual(calc.division(0, -5), 0)
        self.assertEqual(calc.division(0, 0.5), 0)

if __name__ == '__main__':
    unittest.main()
