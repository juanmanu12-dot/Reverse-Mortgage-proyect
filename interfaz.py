import calculadora


try:
    #obtenemos los datos de entrada
    propiedad  = float (input("ingrese el valor de la propiedad: "))
    plazo      = int (input ("ingrese el numero de cuotas: "))
    tasa       = float(input ("ingrese la tasa de interes: "))
    prestamo   = float(input("ingrese la tasa de prestamo"))
    # realizar el proceso
    cuota_mensual = calculadora.cuota_mensual( propiedad, tasa, plazo, prestamo)
    #mostrar los datos de salida 

    print(f"el valor de la cuota es : {cuota_mensual}")
    
except (ValueError, calculadora.Errorcompra, calculadora.Errortasa, calculadora.Errorprestamo, calculadora.ErrorplazoCero) as e:
    print(e)
    print("por favor verifique los datos ingresados" )
