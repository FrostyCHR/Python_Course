#---------------------------------------------------------------MÉTODOS DE LISTS---------------------------------------------------------------#

list1 = ["Table", 72, False, "Length"]
list2 = ["Pape", False, ["Dalto", 95], "Pedro"]
list3 = ["Pape", False, ["Dalto", 95], "Pedro"]
list_num = [True,0,314,245,2.1,5153,True,-1,12.5,False,-51.23124, 59.52,-2.5]


# list: (Función, no método)
# Crea una lista. Debe recibir como parámetro otra lista (what!?), una tupla, un set (se hará aleatorio el orden), un diccionario o un string.

print(list("Hola, Pedro")) # Un elemento por caracter.
print(list()) # Lista vacía. O simplemente: lista = []


# len: (Es una función, NO método)
# Devuelve la cantidad de elementos de una lista. (similar a .length en JS)

print(len(list1))



# ADICIÓN DE ELEMENTOS:

# append:
# Añade un elemento al final de una lista. (similar a .push() en JS)

print(list1.append("Last")) # No devuelve nada.
print(list1) # Modifica la lista.


# insert:
# Añade un elemento a una lista en el índice especificado.

list1.insert(1,"Posición 1") # Ocupa el índice 1 y todo se va una posición a la derecha.
print(list1)


# extend:
# Añade una lista a otra como elementos individuales.

list1.extend(["Jorge", 42])
print(list1)


# DIFERENCIA ENTRE APPEND Y EXTEND:

list2.append(["1",2]) # Añade la lista como una lista (1 solo elemento).
list3.extend(["1",2]) # "Rompe" la lista y añade cada uno de sus elementos (como si ya llevase un spread (...) incorporado).

print(list2)
print(list3)



# ELIMINACIÓN DE ELEMENTOS:

# pop:
# Elimina el elemento del índice especificado (-1 es el último, -2 el penúltimo...).

print(list1)
print(list1.pop(-2)) # Devuelve el elemento eliminado.
print(list1)


# remove:
# Elimina un elemento de la lista por su valor. Si no lo encuentra, lanza una excepción.

list1.remove(False) # Esto no devuelve nada.
print(list1)


# clear:
# Elimina TODOS los elementos de una lista.

list3.clear()
print(list3)



# ORDENACIÓN DE ELEMENTOS:

# sort:
# Ordena una lista íntegramente conformada por números y booleans de menor a mayor. Si ponemos reverse=True en el argumento, se pone al revés.

list_num.sort(reverse=True)
print(list_num) # Negativos --> 0 --> False --> True --> Positivos


# reverse:
# Invierte el orden de una lista. (No tiene por qué estar ordenada.)

list2.reverse()
print(list2)


# index:
# Funciona igual que en los strings. Busca un elemento y devuelve la posición en la que se encuentra.

print(list2.index("Pape"))



# INFORMACIÓN SOBRE TUPLAS Y SETS:

# TUPLAS:
# Este tipo de dato es inmutable (no modificable, solo se puede redefinir), por lo que no tiene muchos métodos (count e index). (usar dir() para confirmarlo)

# SETS:
# En este tipo de dato solo se puede usar pop y remove. (usar dir() para confirmarlo)