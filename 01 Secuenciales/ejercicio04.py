#EJERCICIO 04:

'''Desarrolle un algoritmo que permita ingresar 5 notas de un alumno y devuelva el promedio 
y si está aprobado o no, diseñe el diagrama de flujo. Se considera aprobado con una nota 
mayor o igual a 6.

Tip: El promedio se calcula sumando todas las notas y dividiendo el resultado por la 
cantidad de notas.

Ejemplo:
Las notas son: 6 - 6 - 6 - 6 - 5
Sumamos las notas: 6+6+6+6+5 = 29
Dividimos el resultado por la cantidad de notas (5 notas): 29/5 = 5,8
5,8 es el promedio de notas (Desaprobado)'''

suma = 0
suma = suma + float(input("Ingresa la nota 1: "))
suma = suma + float(input("Ingresa la nota 2: "))
suma = suma + float(input("Ingresa la nota 3: "))
suma = suma + float(input("Ingresa la nota 4: "))
suma = suma + float(input("Ingresa la nota 5: "))
promedio = suma / 5
print("El promedio es:", promedio)
if promedio >= 6:
    print("Estado: Aprobado")
else:
    print("Estado: Desaprobado")