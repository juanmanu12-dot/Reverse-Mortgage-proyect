
class Errorcompra(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el valor de la propiedad no puede ser cero")

class Errortasa(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: la tasa de interés no puede ser cero o negativa")

class Errorprestamo(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el porcentaje del préstamo no puede superar el 60%")

class ErrorplazoCero(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el plazo del préstamo no puede ser 0 años")
        
def cuota_mensual(propiedad, prestamo, tasa, plazo):
    if propiedad <= 0:
        raise Errorcompra()
    elif tasa <= 0:
        raise Errortasa()
    elif prestamo > 0.60:  # regla del 60%
        raise Errorprestamo()
    elif plazo <= 0:
        raise ErrorplazoCero()
    else:
        return (propiedad * prestamo) / (
            (1 - (1 + tasa/12) ** (-plazo * 12)) / (tasa/12)
        )

if __name__ == "__main__":
    # ==== PRUEBAS ====
    # Caso 1: propiedad = 0 → Errorcompra
    try:
        print(cuota_mensual(0, 0.5, 0.02, 10))
    except Exception as e:
        print(e)

    # Caso 2: tasa = 0 → Errortasa
    try:
        print(cuota_mensual(100000, 0.5, 0, 10))
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
        print(cuota_mensual(100000, 0.5, 0.02, 10))
    except Exception as e:
        print(e)



