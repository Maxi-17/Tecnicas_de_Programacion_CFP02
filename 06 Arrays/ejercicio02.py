#EJERCICIO 02:

'''Ingresar 10 valores numéricos en un array y mostrar cuantos son pares y cuantos son impares.'''

numeros = []
contPares = 0
contImpares = 0
for i in range(10):
    num = int(input(f"Ingresa el valor para la posicion {i+1}: "))
    numeros.append(num)
for n in numeros:
    if n % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

print(f"Total pares: {contPares}")
print(f"Total impares: {contImpares}")