#---------------------------------------------------------------MÉTODOS DE CADENAS---------------------------------------------------------------#

# ¿Qué es un método?
# Es una función (codigo que se ejecuta en base a unos parámetros) relacionada con un objeto.

string1 = "hay que poner algo, así que pongo esto. Pedro"
string2 = "No estoy satisfecho con mi instituto, así que me voy a ir."
num = "5208"
alpha = "holasoyalphanumeric"


# dir: (Es una función, NO método)
# Devuelve una lista de todos los atributos de un objeto.

print(dir(string1))


# len: (Es una función, NO método)
# Devuelve la cantidad de caracteres de un string. (similar a .length en JS)

print(len(string1))



# MAYÚSCULAS Y MINÚSCULAS:

# upper:
# Transforma el string a mayúsculas. (como toUpperCase)

print(string1.upper())


# lower:
# Transforma el string a minúsculas. (como toLowerCase)

print(string1.lower())


# capitalize:
# Transforma la primera letra en mayúsculas, pero también pone el resto en minúscula.

print(string1.capitalize())



# BÚSQUEDA DE ELEMENTOS:

# find:
# Busca una cadena dentro de otra. Retorna la posición (índice) en el que lo encontró por primera vez. Si no lo encuentra, devuelve -1.

print(string1.find("e"))
print(string1.find("z"))


# index:
# Funciona igual que el anterior, pero si no encuentra nada da un error.

print(string1.index("e"))
print(string1.index("t")) # Probar un número.



# "TIPO" DE STRING:

# isnumeric:
# Si es un string con SOLO números, devuelve True, si no, devuelve False. Es muy loco, ya que SOLO se puede aplicar a strings. 

print(num.isnumeric())


# isalpha:
# Es alfa cuando contiene letras a - z, sin otros caracteres como espacios, comas o puntos.

print(alpha.isalpha())



# CARACTERES Y SU FRECUENCIA:

# count:
# Devuelve el número de veces que una cadena se encuentra dentro de otra. Similar a find. Si no encuentra, devuelve 0.

print(string1.count("go")) # 2
print(string1.count("9")) # 0



# VERIFICACIÓN DE INICIO Y FIN:

# startswith:
# Comprueba si la cadena sobre la que lo ejecutamos empieza por la cadena en el argumento. Devuelve valores booleanos. (igual que en JS)

print(string1.startswith("hay "))


# endswith:
# Igual que el anterior, pero al final.

print(string1.endswith("."))



# MODIFICACIÓN:

# replace:
# Sustituye una cadena dada por otra dada dentro de la que ejecuta el método. Si no hay coincidencias, devuelve el string original.

print(string1.replace("hay", "hoy")) # Podemos guardar esto en una variable. (sin print)
print(string1) # No modifica el string original.


# Split:
# Separa la cadena en diferentes elementos de una lista en base al caracter que pongamos como argumento. Devuelve dicha lista. (igual que en JS)

print(string1.split(" ")) # Podemos guardar esto en una variable. (sin print)
print(string1) # No modifica el string original.