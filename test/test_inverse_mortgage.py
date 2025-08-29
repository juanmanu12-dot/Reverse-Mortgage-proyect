import sys 
sys.path.append("src")
import unittest
from model import calculadora


class TestInverseMortgage(unittest.TestCase):
    
    def test_renta_mensual(self):
        propiedad = 3500000_00
        prestamo = 40/100
        tasa = 10/100
        plazo = 15

        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )

        renta_esperada = 1504447.16
        
        self.assertAlmostEqual(renta_esperada, renta_calculada, 2)


    def test_renta_mensual_2(self):
        propiedad = 200000000
        prestamo = 35/100
        tasa = 11/100
        plazo = 12
    
        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )
    
        renta_esperada = 1875301.89
    
        self.assertAlmostEqual( renta_esperada, renta_calculada,2)


    def test_cuota_mensual_3(self):
        propiedad = 600000000
        prestamo = 50/100
        tasa = 10.50/100
        plazo = 20
    
        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )
    
        renta_esperada = 2995140.66
    
        self.assertAlmostEqual( renta_esperada, renta_calculada,2)


    def  test_maximo_permitido(self):
        propiedad = 1500000000
        prestamo = 60/100
        tasa = 12/100
        plazo = 25
    
        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )
    
        renta_esperada = 9479017.28
    
        self.assertAlmostEqual( renta_esperada, renta_calculada)

   
    def test_minimo_permitido(self):
        propiedad = 80000000
        prestamo =30/100
        tasa = 9/100
        plazo = 10
        
        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )
        renta_esperada =  304021.86
        self.assertAlmostEqual( renta_esperada, renta_calculada,2)

    
    def test_plazo_minimo(self):
        propiedad = 600000000
        prestamo = 50/100
        tasa = 12/100
        plazo = 5
        renta_calculada = calculadora.renta_mensual(propiedad,prestamo, tasa, plazo )
        renta_esperada =  6597782.21
        self.assertAlmostEqual( renta_esperada, renta_calculada,2)


    
    def test_Error_compra(self):
        propiedad = 0
        prestamo = 50/100
        tasa = 10/100
        plazo = 15
        
        with self.assertRaises(calculadora.Errorcompra):
            renta_mensual = calculadora.renta_mensual(propiedad, prestamo, tasa, plazo)

    def test_Error_prestamo(self):
        propiedad = 200000000
        prestamo = 60/100
        tasa = 10/100
        plazo = 20
        
        with self.assertRaises(calculadora.ErrorPrestamo):
            renta_mensual = calculadora.renta_mensual(propiedad, prestamo, tasa, plazo)
    
    def test_Error_tasa(self):
        propiedad = 150000000
        prestamo = 50/100
        tasa = -5/10
        plazo = 10
        
        with self.assertRaises(calculadora.ErrorTasa): 
            renta_mensual = calculadora.renta_mensual(propiedad, prestamo, tasa, plazo)
            
    def test_Error_plazo(self):
        
        propiedad = 120000000
        prestamo = 40/10
        tasa = 12/0
        plazo = 0
        
        with self.assertRaises(calculadora.ErrorPlazo):
            renta_mensual = calculadora.renta_mensual(propiedad, prestamo, tasa, plazo)
                    
if __name__ == '__main__':
    unittest.main()