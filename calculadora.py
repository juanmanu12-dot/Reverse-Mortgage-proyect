def cuota_mensual(propiedad,prestamo, tasa, plazo):
    return (propiedad * prestamo) / ((1-(1+tasa/12)**(-plazo*12))/(tasa/12))

  
def prueba_caso_normal_1():

    propiedad = 350_000_000
    prestamo = 40/100
    tasa = 10/100
    plazo = 15

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 1_504_447

    if(round(cuota_calculada,0) == round(cuota_esperada,0)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")


def prueba_caso_normal_2():
    propiedad = 200_000_000
    prestamo = 35/100
    tasa = 11/100
    plazo = 12

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 1_504_447

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")

 
def prueba_caso_normal_3():

    propiedad = 600000000
    prestamo = 50/100
    tasa = 10.50/100
    plazo = 20

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 2995140_66

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")
prueba_caso_normal_1()
prueba_caso_normal_2()
prueba_caso_normal_3()

