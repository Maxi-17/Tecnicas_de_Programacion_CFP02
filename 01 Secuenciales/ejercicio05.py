#EJERCICIO 05:

'''Desarrolle un algoritmo que me muestre cuanto debo pagar de interes un celular de $50.000 con
tarjeta de credito, dependiendo de la cantidad de cuotas que elija.
Si pago en 1 cuota no sumo interes
Si pago de 2 a 3 cuotas sumo un interes del 20%
Si pago de 4 a 6 cuotas sumo un interes del 40%
Si pago de 7 cuotas en adelante sumo un interes del 50%'''

precioOriginal = 50000
cuotas = int(input("Ingresa la cantidad de cuotas: "))
if cuotas == 1:
    interes = 0
elif cuotas >= 2 and cuotas <= 3:
    interes = 0.20  
elif cuotas >= 4 and cuotas <= 6:
    interes = 0.40  
else: 
    interes = 0.50  
montoInteres = precioOriginal * interes
precioFinal = precioOriginal + montoInteres

print("Intereses a pagar: $", montoInteres)
print("Precio total con intereses: $", precioFinal)