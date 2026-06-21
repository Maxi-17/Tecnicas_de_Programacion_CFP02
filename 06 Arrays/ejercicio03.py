#EJERCICIO 03:

'''Hacer un programa que permita ingresar 10 valores a un array seguido muestre cuantos son 
positivos, cuantos negativos y cuantos son nulos.'''

numeros = []
cPos = 0
cNeg = 0
cNulo = 0
for i in range(10):
    num = float(input(f"Ingresa el valor para la posición {i+1}: "))
    numeros.append(num)
for n in numeros:
    if n > 0:
        cPos += 1
    elif n < 0:
        cNeg += 1
    else:
        cNulo += 1

print(f"Positivos: {cPos}")
print(f"Negativos: {cNeg}")
print(f"Nulos: {cNulo}")