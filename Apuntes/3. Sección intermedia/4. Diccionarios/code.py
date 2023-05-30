#---------------------------------------------------------------DICCIONARIOS---------------------------------------------------------------#

# Este es un tipo de dato compuesto que se caracteriza por tener llaves (propiedades), y valores. En cuanto a sintaxis, son iguales a los JSON en JS.


# Diccionarios vacíos:

dict_empty1 = dict()
dict_empty2 = {}

print(dict_empty1,dict_empty2)


# Diccionarios con dict:

dict1 = dict(nombre="Lucas", apellido="Dalto")

print(dict1)


# Diccionarios con {}:

dict2 = {
    ("Hola", "sí"): "Puede ser",
    frozenset({1,2,3}): 5,
    # ["1","2"]: False No se pueden poner listas como keys, pero tuplas y frozensets sí.
}

print(dict2)


# Diccionarios con fromkeys() (todos los valores vacíos):

dict3 = dict.fromkeys("Nombre", "Apellido") # Itera el primer elemento y pone como valor el segundo. Solo 2 argumentos.
dict4 = dict.fromkeys(["Nombre", "Apellido", "Trabajo"])

print(dict3)
print(dict4)