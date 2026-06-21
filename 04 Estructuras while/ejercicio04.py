#EJERCICIO 04:

'''Realiza un algoritmo que muestre los primeros 100 numeros enteros iniciando desde el
numero que el usuario ingreso.
Ejemplo: Si ingreso el numero 1 deberia mostrar los primeros 100 numeros siguientes. Entonces
en este caso mostraria los numeros del 2 al 101'''

num = int(input("Ingresa un numero inicial: "))
num = num +1
contador = 1
while contador <= 100:
    print(num)     
    num += 1
    contador += 1
