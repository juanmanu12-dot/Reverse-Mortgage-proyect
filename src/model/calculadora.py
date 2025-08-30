class Errorcompra(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el valor de la propiedad no puede ser cero")

class Errortasa(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: la tasa de interés no puede ser menor al 9 o mayor al 12 por ciento anual")

class Errorprestamo(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el porcentaje del préstamo no puede ser mayor al 100% ni menor o igual a 0")

class Erroredad(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: la edad debe estar entre 65 y 90 años")

class Errorplazo(Exception):
    def __init__(self, *args):
        super().__init__("ERROR: el plazo calculado a partir de la edad debe ser al menos 5 años")


def hipoteca_inversa(propiedad, prestamo, tasa, edad):
    if propiedad <= 0:
        raise Errorcompra()
    elif tasa < 9/100 or tasa > 12/100:  
        raise Errortasa()
    elif prestamo <= 0 or prestamo > 1.0:  
        raise Errorprestamo()
    elif edad < 65 or edad > 90:  
        raise Erroredad()
    else:
        # Plazo definido por la edad (hasta 90 años)
        plazo = 90 - edad  
        if plazo < 5:
            raise Errorplazo()

        # Monto máximo del préstamo sobre la propiedad
        monto_prestamo = propiedad * prestamo  

        # Renta mensual que recibe el titular
        renta = monto_prestamo * (tasa/12) / (1 - (1 + tasa/12) ** (-plazo * 12))

        # Deuda acumulada al final del plazo (fallecimiento simulado)
        deuda_final = renta * plazo * 12  

        # Evaluar si conviene vender o no
        if deuda_final > propiedad:
            recomendacion = "Conviene entregar la vivienda al banco (la deuda supera el valor de la propiedad)."
        else:
            recomendacion = "Conviene vender la vivienda (valor de la propiedad es mayor que la deuda)."

        return {
            "renta_mensual": renta,
            "plazo": plazo,
            "deuda_final": deuda_final,
            "valor_propiedad": propiedad,
            "opciones_herederos": [
                "Vender la vivienda y pagar deuda",
                "Pagar deuda con otros recursos",
                "Entregar la vivienda al banco"
            ],
            "recomendacion": recomendacion
        }




