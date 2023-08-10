# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***

numero = input("Introduce un numero para generar un triángulo rectángulo: ")
while numero.isnumeric() == False:
    numero = input("Introduce un numero para generar un triángulo rectángulo: ")
numero = int(numero)

[print("*"*(n+1)) for n in range(numero)]