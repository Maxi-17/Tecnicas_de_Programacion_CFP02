#EJERCICIO 04:

'''Pedir al usuario ingresar 4 nombres (almacenarlo en un array) y 4 edades (debes almacenarlo en 
otro array) y mostrar cuales de las personas son menores de edad (menor de 18 años) y cuales son 
mayores'''

nombres = []
edades = []
for i in range(4):
    nom = input(f"Ingresaa el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingresa la edad de {nom}: "))
    nombres.append(nom)
    edades.append(edad)
print("\n--- Resultados ---")
for i in range(4):
    if edades[i] < 18:
        print(f"{nombres[i]} es menor de edad")
    else:
        print(f"{nombres[i]} es mayor de edad")