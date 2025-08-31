import sys 
sys.path.append("src")
from model import calculadora

try:
    # primero pedimos la edad
    edad = int(input("Ingrese la edad del solicitante: "))

    # luego pedimos el resto de datos
    propiedad  = float(input("Ingrese el valor de la propiedad: "))
    plazo      = int(input("Ingrese el número de años del préstamo (entre 5 y 25): "))
    tasa       = float(input("Ingrese la tasa de interés anual (%): "))
    prestamo   = float(input("Ingrese el porcentaje de préstamo: "))

    # validaciones con la edad
    if edad < 65:
        raise ValueError("❌ El solicitante debe tener al menos 65 años para acceder a la hipoteca inversa.")
    
    if edad + plazo > 100:
        raise ValueError(f"❌ Con {edad} años y un plazo de {plazo}, se superarían los 100 años permitidos.")

    # realizar el proceso
    cuota_mensual = calculadora.cuota_mensual(propiedad, prestamo, tasa, plazo)

    # mostrar los datos de salida 
    print("\n✅ Resultados de la simulación:")
    print(f"- Cuota mensual: ${cuota_mensual:,.2f}")
    print(f"- Edad del solicitante al final del contrato: {edad + plazo} años")

except (ValueError, calculadora.ErrorCompra, calculadora.ErrorTasa, 
        calculadora.ErrorPrestamo, calculadora.ErrorPlazo) as excepciones:
    print(excepciones)
    print("⚠️ Por favor verifique los datos ingresados.")





