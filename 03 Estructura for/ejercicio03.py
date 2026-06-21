#EJERCICIO 03:

'''Realizar un algoritmo en el cual se muestre cuales numeros son pares e impares partiendo del 
1 al 20'''

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")