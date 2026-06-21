#EJERCICIO 02:

'''Promedio de notas. Dado N (Cantidad indeterminada) notas, calcular el promedio de las notas.
Tip: Para calcular el promedio recuerden hacer la suma de las notas y dividir ese resultado por 
la cantidad de notas 
Ejemplo: Si ingreso 3 notas y son: 6 - 8 - 9 deberia hacer la suma de esas notas y dividir ese 
resultado por la cantidad de notas que es 3. El calculo quedaria asi: (6+8+9) / 3 = 7,6'''

suma = 0
cantidad = 0
nota = float(input("Ingresa una nota (o 0 para terminar): "))
while nota != 0:
    suma += nota          
    cantidad += 1         
    nota = float(input("Ingresa otra nota (o 0 para terminar): "))
if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio de las {cantidad} notas es: {promedio}")
else:
    print("No ingresaste notas")