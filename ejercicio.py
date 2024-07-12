# #Desarrollar un programa en Python que solicite al usuario su nombre, edad y un número, y luego realice operaciones básicas con estos
# datos.

# Requisitos:
#     1. El programa debe solicitar al usuario que ingrese su nombre.
#     2. El programa debe solicitar el usuario que ingrese su edad
#     3. El programa debe mostrar un mensaje de bienvenida utilizando el nombre y la edad proporcionados
# por el usuario
#     4. El programa debe solicitar al usuario que ingrese un número
#     5. El programa debe convertir el número ingresado a un tipo de dato entero
#     6. El programa debe mostrar el doble del número ingresado

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))

print("\n\tBienvenido " + nombre + " con edad " + str(edad) + " anios.")

numero = input("Digite un numero: ")
numero = int(numero)
print(numero * 2)