#EJERCICIO 01:

'''Hacer un programa que calcule la suma de los N primeros números naturales, dónde N es el 
número límite ingresado por teclado.
Ejemplo: Si el usuario ingresa el numero 4 deberia hacer la suma de todos los numeros naturales desde 
el 1 al 4.
El calculo deberia ser de esta manera: 1 + 2 + 3 + 4 = 10.
Finalmente muestro el resultado por pantalla que en este caso seria 10'''

n = int(input("Ingresa el numero limite (N): "))
i = 1
suma = 0
while i <= n:
    suma = suma + i
    i = i + 1  

print(f"La suma de los numeros naturales hasta {n} es: {suma}")