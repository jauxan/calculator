import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicar(self):
        calculadora = Calculadora()
        resultado = calculadora.multiplicar(2, 3)
        self.assertEqual(resultado, 6)

if __name__ == '__main__':
    unittest.main()
