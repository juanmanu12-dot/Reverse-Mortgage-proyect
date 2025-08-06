import unittest
import calculadora


class TestInverseMortgage(unittest.TestCase):
    
    def test_cuota_mensual(self):
        propiedad = 350000000
        prestamo = 40/100
        tasa = 10/100
        plazo = 15

        cuota_calculada = calculadora.cuota_mensual(propiedad,prestamo, tasa, plazo )

        cuota_esperada = 1504447.16
        
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

if __name__ == '__main__':
    unittest.main()