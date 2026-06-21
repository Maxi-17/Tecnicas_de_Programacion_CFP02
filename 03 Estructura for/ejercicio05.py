#EJERCICIO 05:

'''Realizar un programa para ingresar desde el teclado 20 números. Al finalizar mostrar por 
pantalla el numero mayor y el numero menor'''

mayor = 0
menor = 0
for i in range(1, 6):
    num = int(input("Ingresa un numero: "))    
    if i == 1:
        mayor = num
        menor = num
    else:        
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")