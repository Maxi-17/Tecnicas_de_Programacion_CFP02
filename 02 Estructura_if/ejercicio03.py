#EJERCICIO 03:

'''Elaborar un algoritmo donde se ingrese por teclado un número natural de hasta 2 cifras, si tiene 
una cifra muestre lo mínimo que le falta para ser un número de 2 cifras; de lo contrario muestre lo 
mínimo que le falta para ser un número de 3 cifras. Considerar que el usuario ingresa números de hasta 
dos cifras.

Ejemplo:
Ingreso el numero 8
A el 8 le faltan 2 para llegar al numero de dos cifras mas próximo (10)
Muestro por pantalla el numero 2'''

numero = int(input("Ingresa un numero natural (hasta 2 cifras): "))
if numero < 10:    
    falta = 10 - numero
    print("Al", numero, "le faltan", falta, "para ser un numero de dos cifras.")
else:    
    falta = 100 - numero
    print("Al", numero, "le faltan", falta, "para ser un numero de tres cifras.")
    