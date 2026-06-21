#EJERCICIO 2:

'''Los padres de un niño le prometieron darle 10 dólares cuando cumpliera 12 años de
edad y duplicar el regalo en cada cumpleaños subsiguiente hasta que el regalo excediera 
1000 dólares. Escriba un programa para determinar qué edad tendrá el niño cuando se le dé la 
última cantidad y la cantidad total recibida.'''

edad = 12
regalo = 10
totalRecibido = 0
while regalo <= 1000:
    totalRecibido += regalo
    if regalo * 2 <= 1000:
        edad += 1
        regalo *= 2
    else:
        break

print(f"El niño tendra {edad} años cuando reciba el ultimo regalo")
print(f"La cantidad total recibida es de: {totalRecibido} dolares")