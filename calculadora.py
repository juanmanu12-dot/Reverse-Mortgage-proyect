class ErrorValorPropiedad(Exception):
    pass
class ErrorTasa(Exception):
    pass
class ErrorPlazo(Exception):
    pass
class ErrorPrestamo(Exception):
    pass


def cuota_mensual(propiedad,prestamo, tasa, plazo):

    if propiedad  < 80000000:
        raise ErrorValorPropiedad("El valor de la propiedad no puede ser menor a $80.000.000")
    
    if tasa < 0.09 or tasa > 0.12:
        raise ErrorTasa("La tasa de interes debe estar entre 9% y 12%")
    
    if plazo < 5 or plazo > 25:
        raise ErrorPlazo("El plazo debe estar entre 5 y 25 años")
    
    if prestamo < 0.3 or prestamo > 0.6:
        raise ErrorPrestamo("El porcentaje de prestamo debe estar entre 30% y 60%")
    else :
        return (propiedad * prestamo) / ((1-(1+tasa/12)**(-plazo*12))/(tasa/12))

def monto_total_prestamo(propiedad, prestamo):

    if propiedad < 80000000:
        raise ErrorValorPropiedad("El valor de la propiedad no puede ser menor a $80.000.000")
    if prestamo < 0.3 or prestamo > 0.6:
        raise ErrorPrestamo("El porcentaje de prestamo debe estar entre 30% y 60%")
    else:
        return propiedad * prestamo

def total_meses(plazo):
    if plazo < 5 or plazo > 25:
        raise ErrorPlazo("El plazo debe estar entre 5 y 25 años")
    else:
        return plazo * 12

def tasa_mensual(tasa):
    if tasa < 0.09 or tasa > 0.12:
        raise ErrorTasa("La tasa de interes debe estar entre 9% y 12%")
    else:
        return tasa / 12

def costo_total(propiedad, prestamo, tasa, plazo):
    cuota = cuota_mensual(propiedad, prestamo, tasa, plazo)
    meses = total_meses(plazo)
    return cuota * meses

def intereses_totales(propiedad, prestamo, tasa, plazo):
    cuota = cuota_mensual(propiedad, prestamo, tasa, plazo)
    meses = total_meses(plazo)
    monto_prestamo = monto_total_prestamo(propiedad, prestamo)
    return (cuota * meses) - monto_prestamo
