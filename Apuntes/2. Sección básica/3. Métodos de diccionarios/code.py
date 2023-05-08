#---------------------------------------------------------------MÉTODOS DE DICCIONARIOS---------------------------------------------------------------#

dict1 = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 650000
}



# keys:
# Devuelve un tipo de dato llamado "dict_keys" que contiene lo que parece ser una lista con todas las entradas del diccionario (propiedades en JS). Sirve para iterar las keys (veremos esto más adelante).

print(type(dict1.keys()))
print(dict1.keys())


# get:
# Devuelve el valor del key especificado.

print(dict1.get('subs')) # Esto dice None si no encuentra nada.
print(dict1["subs"]) # Esto lanza una excepción si no encuentra nada.


# clear:
# Elimina todo el diccionario.

#dict1.clear()
#print(dict1)


# pop:
# Elimina un elemento (key) de un diccionario.

dict1.pop("apellido", "subs") # Solo quita uno, pero no lanza ninguna excepción.
print(dict1)


# items:
# Devuelve un objeto de tipo dict_items que se puede iterar.

print(dict1.items())