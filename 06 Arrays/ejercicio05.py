#EJERCICIO 05:

'''Dado un array que contenga 10 numeros y un numero ingresado por el usuario, mostrar los elementos 
(numeros del array) que son mayores que el numero ingresado''' 

numeros = []
for i in range(10):
    val = float(input(f"Ingresa el valor para la posicion {i+1}: "))
    numeros.append(val)
ref = float(input("Ingresa el numero con el que deseas comparar: "))
print(f"Los numeros del array mayores a {ref} son:")
for n in numeros:
    if n > ref:
        print(n)