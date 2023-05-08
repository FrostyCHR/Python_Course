#---------------------------------------------------------------INPUTS---------------------------------------------------------------#

# Un input es un elemento que permite la introducción de datos dentro de un programa informático.

# La función input es la que nos permite hacer esto en Python. SIEMPRE devuelve un string.


# Con textos:

nombre = input("Introduce tu nombre. ") # Es importante dejar un espacio al final para que se vea mejor.

print("¿El input se espera a que respondas para seguir con el programa?") # Sí.

print(f"Tu nombre es {nombre}.")


# Con números:

# Enteros:
numero_entero = input("Introduzca un número entero. ")

print(numero_entero*2) # Concatena, ya que numero es un string. "6"*2 = "66"; 6*2 = 12.

print(int(numero_entero)*2) # Esta es la manera correcta. int lo transforma a tipo numero entero.


# Racionales:
numero_decimal = input("Introduzca un número con decimales. ")

print(float(numero_decimal)*2)