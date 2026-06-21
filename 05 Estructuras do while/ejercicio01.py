#EJERCICIO 01:

'''Determinar en un conjunto de n números naturales: 
¿ Cuántos son menores que 15 ?
¿ Cuántos son mayores que 50 ?
¿ Cuántos están en el rango entre 25 y 45 ?.
Para salir del bucle ingresar la letra x'''

contMenores = 0
contMayores = 0
contRango = 0
while True:
    entrada = input("Ingresa un numero (o 'x' para salir): ")
    if entrada.lower() == 'x':
        break
    numero = float(entrada)    
    if numero < 15:
        contMenores += 1
    elif numero > 50:
        contMayores += 1
    elif 25 <= numero <= 45:
        contRango += 1

print(f"Menores que 15: {contMenores}")
print(f"Mayores que 50: {contMayores}")
print(f"En el rango 25-45: {contRango}")