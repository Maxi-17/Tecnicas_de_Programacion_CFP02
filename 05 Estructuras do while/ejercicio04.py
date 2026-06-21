#EJERCICIO 04:

'''En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente 
se conoce: número de cuenta y saldo actual. El ingreso de datos debe finalizar al ingresar un valor 
negativo en el número de cuenta. 
Se pide realizar un programa que lea los datos de las cuentas corrientes e informe:
a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que:
Estado de la cuenta 'Acreedor' si el saldo es >0. 
'Deudor' si el saldo es <0.
'Nulo' si el saldo es =0.
b) La suma total de los saldos acreedores.'''


sumaAcreedores = 0
numCuenta = int(input("Ingresa numero de cuenta (negativo para salir): "))
while numCuenta >= 0:
    saldo = float(input(f"Ingresa el saldo de la cuenta {numCuenta}: "))
    if saldo > 0:
        print("Estado: Acreedor")
        sumaAcreedores += saldo
    elif saldo < 0:
        print("Estado: Deudor")
    else:
        print("Estado: Nulo")
    numCuenta = int(input("Ingrese el siguiente número de cuenta (negativo para salir): "))

print(f"La suma total de los saldos acreedores es: ${sumaAcreedores}")