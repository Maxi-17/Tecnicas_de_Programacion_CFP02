#EJERCICIO 01:

'''Ingresar 3 numeros en un array vacio. Luego hacer las suma de esos tres
elementos y guardar el resultado en un nuevo array'''

numeros = []
resultado = []
for i in range(3):
    num = int(input(f"Ingresa el numero {i+1}: "))
    numeros.append(num)
suma = sum(numeros)
resultado.append(suma)

print(f"El array de resultados es: {resultado}")