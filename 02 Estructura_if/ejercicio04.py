#EJERCICIO 04:

'''Crear un algoritmo que me pida ingresar si quiero comprar libros o cuadernos (solo puedo elegir 
una opcion). Luego le debo pedir que ingrese la cantidad de articulos a comprar. En funcion de la 
cantidad debo aplicar un descuento . Debo mostrar por pantallla el valor original (Sin descuento
aplicado), el descuento y el valor final (Con el descuento aplicado)
Datos:
Cuaderno:
Precio por unidad: $250
De 1 a 12 articulos no hay descuento
De 13 a 24 articulos hay 10% de descuento
De 25 articulos en adelante hay un 30% de descuento
Libro:
Precio por unidad: $500
De 1 a 12 articulos no hay descuento
De 13 a 24 articulos hay 10% de descuento
De 25 articulos en adelante hay un 30% de descuento'''

producto = input("Deseas comprar 'libro' o 'cuaderno'?: ").lower()
cantidad = int(input("Ingresa la cantidad de articulos: "))
if producto == "cuaderno":
    precioUnitario = 250
elif producto == "libro":
    precioUnitario = 500
else:
    print("Producto no valido")
    precioUnitario = 0

if precioUnitario > 0:
    valorOriginal = precioUnitario * cantidad
    if cantidad >= 25:
        descuentoPorcentaje = 0.30
    elif cantidad >= 13:
        descuentoPorcentaje = 0.10
    else:
        descuentoPorcentaje = 0        
    valorDescuento = valorOriginal * descuentoPorcentaje
    valorFinal = valorOriginal - valorDescuento
    print("Valor original: $", valorOriginal)
    print("Descuento: $", valorDescuento)
    print("Valor final: $", valorFinal)