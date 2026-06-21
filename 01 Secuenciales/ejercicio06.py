#EJERCICIO 06:

'''Escribe un programa que pregunte al usuario si es culpable o no. Asumiremos que:
En caso afirmativo el usuario responderá si En caso contrario responderá no.
Si el usuario responde si se escribirá “Irás a la cárcel”.
Si el usuario responde no se escribirá “Eres inocente, puedes ir a casa”.'''

respuesta = input("Sos culpable? (responde si o no): ")
if respuesta == "si":
    print("Vas a la carcel")
else:
    print("Sos inocente, podes ir a casa")