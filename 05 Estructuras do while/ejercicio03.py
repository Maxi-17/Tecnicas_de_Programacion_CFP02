#EJERCICIO 03:

'''Realizar un programa en el que el usuario (cajero) ingrese el total de la compra de un cliente. 
Luego se debera ingresar el valor de los cupones de descuento del cliente para aplicarlos sobre 
el total de la compra (Cuando no se quiera ingresar mas cupones ingresar la letra x).
Finalmente mostrar por pantalla el total de la compra con el descuento aplicado'''

totalCompra = float(input("Ingresa el total de la compra: "))
while True:
    entrada = input("Ingresa el valor del cupoon (o 'x' para terminar): ")
    if entrada.lower() == 'x':
        break  
    valorCupon = float(entrada)
    totalCompra -= valorCupon
    
    print(f"Cupón aplicado. Nuevo total: ${totalCompra}")

print(f"El total final de la compra es: ${totalCompra}")