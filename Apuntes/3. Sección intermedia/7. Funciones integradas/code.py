#---------------------------------------------------------------FUNCIONES INTEGRADAS---------------------------------------------------------------#

# Esto son partes de código que vienen por defecto en Python orientadas a que los desarrolladores las puedan reutilizar en sus programas. (built-in functions)

# Ventajas de las funciones:
# - Permiten reutilizar código, evitando la repetición y haciendólo más eficiente.
# - Permiten que se pueda probar el código por partes y de manera más fácil. Además, al corregir un error este cambio se ve reflejado en todas las partes en las que se ejecute la función.
# - Permiten que el código sea más fácil de leer. 

# Abstracción: Consiste en entender lo que hacen las funciones integradas y no en entender cómo lo hacen. Ejemplo: len() devuelve la cantidad de caracteres / elementos (según el tipo de dato que pongamos como argumento). ¿Cómo funciona internamente? No lo sé, pero tampoco es necesario saberlo (aunque sería curioso).

numeros = {2,452.24,-4.5,0,2,-1,-54.5}



# max:
# Devuelve el número más grande. (tuplas, listas o conjuntos)

# min:
# Igual, pero con el más pequeño. (tuplas, listas o conjuntos)

print(f"El número más grande es {max(numeros)} y el más pequeño es {min(numeros)}.")

print("------------------------")


# round:
# REDONDEA un float al número de decimales indicados en el segundo argumento.

print(round(14.525352, 4))

print("------------------------")


# bool:
# Devuelve False en caso de poner: 0, [], (), {} (vacíos en general) o False.
# Devuelve True en el resto de casos.

print(bool(0), bool({"Hola", 0, 6.2}))

print("------------------------")


# all:
# Similar al anterior, pero comprueba los datos dentro de un iterable.

print(all({"texto", frozenset({0, 1}), False})) # False por el último elemento, False.
print(all({"texto", frozenset({0, 1}), True}))

print("------------------------")


# sum:
# Suma todos los números de un iterable.

print(sum(numeros))