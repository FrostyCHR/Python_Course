#---------------------------------------------------------------EXPRESIONES REGULARES---------------------------------------------------------------#

# Las expresiónes regulares son una "notación" que nos permite encontrar coincidencias a través del uso de 

import re # Este es el módulo oficial de Python que nos permite trabajar con expresiones regulares.


texto = """Este es un texto de prueba (112) para expresiones_regulares,
Añado otra línea para \hacer pruebas.
Y una 3 123 por el mismo motivo,."""


# Search:
# Solamente dice si se encuentra o no la coincidencia. (No le veo mucha utilidad por el método find o count)

resultado = re.search("2", texto)

print(resultado)

print("------------")


# Findall:
# Devuelve una lista con todas las coincidencias.
# flags=re.IGNORECASE hace que no importe que esté en mayúscula o en minúscula.

todo = re.findall("e", texto, flags=re.IGNORECASE)

print(todo)

print("------------")




# EXPRESIONES REGULARES EN SÍ:


# \d: Busca números del 0-9.

coincidencias = re.findall(r"\d", texto)

print(coincidencias)

print("------------")

# \D: Busca TODO menos números del 0-9. (¿Por qué se pone TODO en azul?)

coincidencias = re.findall(r"\D", texto)

print(coincidencias)

print("------------")



# \w: Busca caracteres alfanuméricos (a-z A-Z 0-9 _).

coincidencias = re.findall(r"\w", texto)

print(coincidencias)

print("------------")

# \W: Busca TODO menos caracteres alfanuméricos.

coincidencias = re.findall(r"\W", texto)

print(coincidencias)

print("------------")



# \s: Busca espacios, tabs y saltos de línea (\n).

coincidencias = re.findall(r"\s", texto)

print(coincidencias)

print("------------")

# \S: Busca TODO menos espacios, tabs y saltos de línea (\n).

coincidencias = re.findall(r"\S", texto)

print(coincidencias)

print("------------")



# \n: Busca saltos en línea.

coincidencias = re.findall(r"\n", texto)

print(coincidencias)

print("------------")

# .: Busca TODO menos saltos en línea.

coincidencias = re.findall(r".", texto)

print(coincidencias)

print("------------")



# \x (x = caracteres con funcionalidad especial en expresiones regularas, como el .): Lo que hace el Alt+92 es cancelar la funcionalidad especial del caracter para buscarlo de manera literal. En el caso del punto, buscaríamos TODO menos saltos en línea, pero al poner \ antes, le decimos que cancele esa funcionalidad y que busque los puntos.

coincidencias = re.findall(r"\.", texto)

print(coincidencias)

print("------------")



# Coincidencia más compleja, que busque un número, seguido de un paréntesis ), seguido de un espacio.

coincidencias = re.findall(r"\d\)\s", texto) # Pongo \ antes de ) para evitar una excepción.

print(coincidencias)

print("------------")



# ^: Busca el inicio del texto. Sirve, por ejemplo, para ver si el texto empieza por Hola.

coincidencias = re.findall(r"^Hola", texto) # (No empieza por Hola.)

print(coincidencias)

print("------------")

# ^ + flags=re.M (o MULTILINE): Igual que sin el parámetro, pero en cada línea.

coincidencias = re.findall(r"^Y", texto, flags=re.M)

print(coincidencias)

print("------------")

# $: Busca el final del texto. Sirve, por ejemplo, para ver si el texto empieza por Hola.

coincidencias = re.findall(r"\.$", texto) # La cadena acaba con .

print(coincidencias)

print("------------")

# $ + flags=re.M (o MULTILINE): Igual que sin el parámetro, pero en cada línea.

coincidencias = re.findall(r",$", texto, flags=re.M)

print(coincidencias)

print("------------")



# {n}: Busca lo que esté a la izquierda de {n} n veces.

coincidencias = re.findall(r"\d{3}", texto) # Esto sirve para buscar un número de 3 cifras. \d{3} = \d\d\d

print(coincidencias)

print("------------")

# {n,m}: Busca lo que esté a la izquierda de {n,m} al menos n veces, y como máximo m veces.

coincidencias = re.findall(r"\d{1,2}", texto)

print(coincidencias)

print("------------")



# (x): Sirve para meter todo lo que esté dentro del paréntesis en un conjunto.

coincidencias_sin_p = re.findall(r"\s\d{2}", texto)

coincidencias_con_p = re.findall(r"(\s\d){2}", texto) # Esto busca espacio número espacio número pero NO lo devuelve. Devuelve espacio número.

print(coincidencias_sin_p, coincidencias_con_p)

print("------------")



# |: Sirve para "ejecutar 2 búsquedas en una sola". Es una puerta OR, una, otra, o las dos.

coincidencias = re.findall(r"\d\s|\w\.", texto)

print(coincidencias) # Devuelve las coincidencias en el orden en el que se encuentran en el string.

print("------------")