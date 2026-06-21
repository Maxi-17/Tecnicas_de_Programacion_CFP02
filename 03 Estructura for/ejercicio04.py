#EJERCICIO 04:

'''Realizar un programa para ingresar desde el teclado 20 números. Al finalizar mostrar por 
pantalla el primer y último valor ingresado.'''

primero = 0
ultimo = 0
for i in range(1, 21):
    num = int(input("Ingresa un numero del 1 al 20: "))    
    if i == 1:
        primero = num    
    ultimo = num
print(f"El primer valor ingresado fue: {primero}")
print(f"El ultimo valor ingresado fue: {ultimo}")