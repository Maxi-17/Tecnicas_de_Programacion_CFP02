#EJERCICIO 03:

'''Desarrolle un algoritmo que me diga el precio total por alquilar una casa de verano segun 
los dias que me hospede.

Si me quedo de 1 a 5 dias me cuesta $3000 c/d.
Si me quedo de 6 a 10 dias me cuesta $2500 c/d.
Si me quedo mas de 11 dias me cuesta $2000 c/d.'''

dias = int(input("Ingresa la cantidad de dias de alquiler: "))
if dias >= 1 and dias <= 5:
    precio_por_dia = 3000
elif dias >= 6 and dias <= 10:
    precio_por_dia = 2500
else:
    precio_por_dia = 2000
total = dias * precio_por_dia
print("El precio total a pagar es:", total)