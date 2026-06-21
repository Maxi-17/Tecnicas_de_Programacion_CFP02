#EJERCICIO 05:

'''Elabora un algoritmo que permita ingresar dos numeros positivos. Debe validar que el segundo
numero ingresado sea mayor que el primero. Luego deben mostrarse por pantalla todos los
numeros pares que se encuentren entre ambos numeros ingresados (solo los numeros pares)
Tip: Para saber si un numero es par se debe calcular el valor del resto al dividir ese numero
por 2. Si el resto es igual a 0, entonces es par'''

num1 = int(input("Ingresa el primer numero positivo: "))
num2 = int(input("Ingresa el segundo numero (tiene q ser mayor al primero): "))
while num2 <= num1:
    print("Error: El segundo numero tiene q ser mayor que el primero")
    num2 = int(input("Ingrese el segundo número nuevamente: "))
print(f"Los numeros pares entre {num1} y {num2} son:")
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)