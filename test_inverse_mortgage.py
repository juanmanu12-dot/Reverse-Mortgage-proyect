import unittest
import calculadora


class TestInverseMortgage(unittest.TestCase):
    
    def test_cuota_mensual(self):
        propiedad = 3500000_00
        prestamo = 40/100
        tasa = 10/100
        plazo = 15

        cuota_calculada = calculadora.cuota_mensual(propiedad,prestamo, tasa, plazo )

        cuota_esperada = 1504447.16
        
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)

if __name__ == '__main__':
    unittest.main()
    def test_cuota_mensual_2(self):
        propiedad = 200000000
        prestamo = 35/100
        tasa = 11/100
        plazo = 12
    
        cuota_calculada = calculadora.cuota_mensual(propiedad,prestamo, tasa, plazo )
    
        cuota_esperada = 1875301.89
    
        self.assertAlmostEqual( cuota_esperada, cuota_calculada,2)
if __name__ == '__main__':
    unittest.main()
    def test_cuota_mensual_3(self):
        propiedad = 600000000
        prestamo = 50/100
        tasa = 10.50/100
        plazo = 20
    
        cuota_calculada = calculadora.cuota_mensual(propiedad,prestamo, tasa, plazo )
    
        cuota_esperada = 2995140.66
    
        self.assertAlmostEqual( cuota_esperada, cuota_calculada,2)
if __name__ == '__main__':



    
    unittest.main()
    def maximo_permitido(self):
        propiedad = 1500000000
        prestamo = 60/100
        tasa = 12/100
        plazo = 25
    
        cuota_calculada = calculadora.cuota_mensual(propiedad,prestamo, tasa, plazo )
    
        cuota_esperada = 9479_017
    
        self.assertAlmostEqual( cuota_esperada, cuota_calculada)
if __name__ == '__main__':
   unittest.main()