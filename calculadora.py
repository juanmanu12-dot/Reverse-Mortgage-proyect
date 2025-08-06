def cuota_mensual(propiedad,prestamo, tasa, plazo):
    return (propiedad * prestamo) / ((1-(1+tasa/12)**(-plazo*12))/(tasa/12))

  
def prueba_caso_normal_1():

    propiedad = 350000000
    prestamo = 40/100
    tasa = 10/100
    plazo = 15

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 1504447.16

    if(round(cuota_calculada,0) == round(cuota_esperada,0)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")


def prueba_caso_normal_2():
    propiedad = 200000000
    prestamo = 35/100
    tasa = 11/100
    plazo = 12

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada =  87748968.89

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

    cuota_esperada = 2995140.66

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")

def maximo_permitido():
    propiedad = 1500000000
    prestamo = 60/100
    tasa = 12/100
    plazo = 25

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 9479017.00

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")



def minimo_permitido():
    propiedad = 80000000
    prestamo = 30/100
    tasa = 12/100
    plazo = 5

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 304022.86

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")
def plazo_minimo():
    propiedad = 600000000
    prestamo = 50/100
    tasa = 12/100
    plazo = 5

    cuota_calculada = cuota_mensual(propiedad,prestamo, tasa, plazo )

    cuota_esperada = 6597782.21

    if(round(cuota_calculada,2) == round(cuota_esperada,2)):
        print("prueba exitosa¡")
    else:
        print("prueba fallida¡")

prueba_caso_normal_1()
prueba_caso_normal_2()
prueba_caso_normal_3()
maximo_permitido()
minimo_permitido()
plazo_minimo()
