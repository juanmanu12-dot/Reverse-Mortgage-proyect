# Calculadora de hipoteca inversa


## Descripcion del proyecto
-El banco entrega al propietario una renta mensual basada en el valor de su vivienda.
-El propietario no paga cuotas durante el contrato.
-Al fallecimiento del titular o al finalizar el plazo, la deuda se liquida con la venta de la propiedad o con recursos de los herederos.
## Entradas
-Valor de la propiedad (COP): precio de la vivienda.
-Porcentaje del préstamo: puede ser de 0% hasta 100% del valor de la propiedad.
-Tasa de interés anual (%): entre 9% y 12%.
-Edad del propietario (años): debe estar entre 65 y 90 años.
-El plazo se calcula automáticamente como 90 - edad (años restantes hasta los 90).
-El plazo mínimo permitido es de 5 años.

## Salidas
-Renta mensual (COP): el monto que recibe el propietario cada mes.
-Plazo del contrato (años): definido según la edad.
-Monto total del préstamo (COP): valor máximo prestado sobre la vivienda.
-Deuda final acumulada (COP): total que debe liquidarse al final del contrato.
-Opciones para herederos:
1Vender la vivienda y pagar la deuda.
2Pagar la deuda con otros recursos.
3Entregar la vivienda al banco.
Recomendación del sistema: sugiere si conviene vender la propiedad o entregarla al banco, comparando el valor de la deuda con el valor de la vivienda.

## Autores
-Esteban Arias Salazar<br>
-Nicol Valeria Atehortua<br>

## instrucciones de uso 
-Clonar el repositorio: https://github.com/estebanariassa/Reverse-Mortgage-proyect.git
-Entrar al proyecto: reverse mortgage
-Ejecutar el programa: python main.py
-Ejecutar pruebas unitarias: python -m unittest discover
## Cómo ejecutar la aplicación en consola



1. Abre la terminal en Visual Studio Code.
2. Navega a la carpeta raíz del proyecto:
   ```
   cd "d:\Descargas D\Reverse_mortgage_calculator\Reverse-Mortgage-proyect"
   ```
3. Ejecuta el archivo principal de la interfaz:
   ```
   python main.py
   ```
4. Ingresa los datos solicitados en la consola para simular la hipoteca inversa.

Esto iniciará la interfaz de consola y podrás realizar simulaciones directamente desde la

## Cómo ejecutar los tests

1. Abre la terminal en Visual Studio Code.
2. Navega a la carpeta del proyecto(Por Ejemplo):
   ```
   cd "d:\Descargas D\Reverse_mortgage_calculator\Reverse-Mortgage-proyect"
   ```
3. Ejecuta el archivo de test con unittest:
   ```
   python -m unittest test/test_inverse_mortgage.py
   ```

Esto ejecutará todas las pruebas y mostrará los resultados
   
   
