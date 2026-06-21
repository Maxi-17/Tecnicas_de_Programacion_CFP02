#EJERCICIO 02:

'''Construir un algoritmo que permita ingresar un número, si el número es mayor de 500, se
debe calcular y mostrar en pantalla el 18% de este.
Tip: Para calcular el porcentaje de un numero solo debo multiplicar el numero por el porcentaje y 
luego dividir ese resultado por 100.
Ejemplo:
Calcular el 20% de 200
Hago 200 * 20 = 4000
Luego hago 4000 / 100 = 40
Entonces el 20% de 200 = 40'''

numero = float(input("Ingresa un numero: "))
if numero > 500:    
    porcentaje = (numero * 18) / 100
    print("El 18% de", numero, "es:", porcentaje)
else:
    print("El numero ingresado no es mayor a 500, no calculo.")