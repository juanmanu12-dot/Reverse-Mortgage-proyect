def cuota_mensual(propiedad,prestamo, tasa, plazo):

    if propiedad == 0:
        raise ValueError("El valor de la propiedad no puede ser cero.")
    
    if tasa == 0:
        return propiedad / plazo
    else :
        return (propiedad * prestamo) / ((1-(1+tasa/12)**(-plazo*12))/(tasa/12))


