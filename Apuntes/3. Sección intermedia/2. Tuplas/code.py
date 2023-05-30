#---------------------------------------------------------------TUPLAS---------------------------------------------------------------#

# Como ya hemos visto antes, una tupla es un tipo de dato compuesto en el que existe un orden, pero no puede ser modificado.
# Son muy útiles para ser leídas, ya que de usan menos recursos que las listas.


# Función tuple:
# Crea una tupla a partir de una lista o de un set.

tupla_con_lista = tuple(["Lucas", "Dalto", 1000000])
tupla_con_set = tuple({"Lucas", "Dalto", 1000000}) # Esto toma un orden aleatorio por las propiedades de los conjuntos.

print(tupla_con_lista, tupla_con_set)


# Creando tuplas sin paréntesis:

tupla_sin_parentesis_0 = "Lucas", "Dalto", 1000000
tupla_sin_parentesis_1 = "Lucas", # Así hay que escribirlo cuando solo hay un dato.

print(tupla_sin_parentesis_0, tupla_sin_parentesis_1)