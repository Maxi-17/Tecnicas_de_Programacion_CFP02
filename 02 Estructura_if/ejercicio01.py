#EJERCICIO 01:

'''Dado un numero ingresado, mostrar si es par o impar.
Tip 1: Saber si un número es par es muy simple, recuerda que los números pares son aquellos que al
dividirlos por 2 el residuo es 0 (2,4,6,8,9,10,12,etc...). Por lo tanto, los números que no pueden 
ser divididos exactamente por 2 son impares.
Tip 2: Podemos usar el operador % que me permite obtener el resto de una division
Ejemplo: Si ingreso el numero 7, deberia hacer 7%2 que me daria igual a 1 (resto de la division). 
Como me dio 1 ya se que el numero 7 es impar'''

numero = int(input("Ingresa un numero entero: "))
if numero % 2 == 0:
    print("El numero", numero, "es par.")
else:
    print("El numero", numero, "es impar.")