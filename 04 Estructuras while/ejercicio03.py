#EJERCICIO 03:

'''Crear un algoritmo donde le pida al usuario crear una contraseña y que la confirme
nuevamente. El bucle termina hasta que el usuario confirme exitosamente la contraseña,
caso contrario se le va a solicitar nuevamente confirmar la contraseña hasta que logre
ingresar la misma'''

clave = input("Crea tu contraseña: ")
confirmacion = input("Confirma tu contraseña: ")
while clave != confirmacion:
    print("Error: Las contraseñas no coinciden. Intentalo nuevamente")
    clave = input("Crea tu contraseña: ")
    confirmacion = input("Confirma tu contraseña: ")

print("Contraseña establecida con exito!")