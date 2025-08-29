
class Errorcompra(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el valor de la propiedad no puede ser cero")

class Errortasa(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: la tasa de interés no puede ser menor al 9 o mayor al 12 por ciento anual")

class Errorprestamo(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el porcentaje del préstamo no puede superar el 60 o menos del 30 por ciento del valor de la propiedad")

class ErrorplazoCero(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el plazo del préstamo no puede ser menor a 5 o mayor a 25 años")
        

def renta_mensual(propiedad, prestamo, tasa, plazo):
    if propiedad <= 0:
        raise Errorcompra()
    elif tasa < 9/100 or tasa > 12/100:  
        raise Errortasa()
    elif prestamo > 0.60 or prestamo < 0.30:  
        raise Errorprestamo()
    elif plazo < 5 or plazo > 25:  
        raise ErrorplazoCero()
    else:
        # Monto máximo del préstamo sobre la propiedad
        monto_prestamo = propiedad * prestamo  

        # cuánto se puede recibir mensualmente
        renta = monto_prestamo * (tasa/12) / (1 - (1 + tasa/12) ** (-plazo * 12))
        
        return renta

if __name__ == "__main__":
    # ==== PRUEBAS ====
    # Caso 1: propiedad = 0 → Errorcompra
    try:
        print(cuota_mensual(0, 0.13, 0.02, 5))
    except Exception as e:
        print(e)

    # Caso 2: tasa = 0 → Errortasa
    try:
        print(cuota_mensual(100000, 0.9, 0, 20))
    except Exception as e:
        print(e)

    # Caso 3: préstamo = 70% → Errorprestamo
    try:
        print(cuota_mensual(100000, 0.7, 0.02, 10))
    except Exception as e:
        print(e)

    # Caso 4: plazo = 0 → ErrorplazoCero
    try:
        print(cuota_mensual(100000, 0.5, 0.02, 0))
    except Exception as e:
        print(e)

    # Caso 5: valores correctos → calcula cuota
    try:
        print(cuota_mensual(100000, 0.5, 0.09, 10))
    except Exception as e:
        print(e)



