#---------------------------------------------------------------FUNCIONES LAMBDA---------------------------------------------------------------#

# (Is this a Half Life reference?)
# Se dice que son como las funciones flecha en JS.

# Forma:

cuadrado_lambda = lambda x: x**2; # Se puede poner más de un parámetro.
# Es una función anónima (pero se guarda en una variable), como esto.
"Hola" # String anónimo, no tiene nombre.


# Lo mismo con una función normal:

def cuadrado_normal(x):
    return x**2

print(f"Lambda: {cuadrado_lambda(2)}. Normal: {cuadrado_normal(2)}.") # Se me acaba de ocurrir que con esto se pueden crear funciones matemáticas como esta.

print("------------------------")



# VENTAJAS DE ESTAS FUNCIÓNES:

# Evitar abrir un bloque de código.
# Una línea menos de código (return automático).
# Ideal para una única expresión.



# FUNCIÓN FILTER (BUILT-IN):
# A partir de una función y de un iterable, añade a otro iterable los elementos que devolvían True en la función.

# Con función normal:

set_numeros = {21,6,3,1,787,23,74,14,7}

def es_par(num):
    if num%2 == 0:
        return True

numeros_pares = filter(es_par,set_numeros)

print(set(numeros_pares)) # Para evitar que sea un filter object hay que transformarlo a lista, set, tupla...


# Con lambda:

numeros_impares = filter(lambda num: num%2 !=0, set_numeros)

print(set(numeros_impares))