#ejercicio 03:

'''Desarrolle un algoritmo que permita ingresar 3 número enteros y devuelva
el número menor y el número mayor.

Ejemplo:
Ingreso los numeros: 5 - 9 - 2
El numero menor es 2
El numero mayor es 9'''

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("El numero mayor es:", mayor)
print("El nu1mero menor es:", menor)