#---------------------------------------------------------------ARCHIVOS TXT---------------------------------------------------------------#

# Para empezar, recordemos que un archivo es simplemente un contenedor de información y que según el formato que tenga, tendrá un tipo de información u otro. (fots, vídeos, texto, hojas de cálculo, audio...)

import os

# Esto nos muestra todo lo que hay en el directorio ("carpeta") en el que nos encontramos. Por algun motivo, estamos en la carpeta Python, y no en 4. Archivos txt.
print(os.listdir())

# Hay que poner la ruta relativa al directorio en el que estamos, es decir, desde que la ruta es diferente para el archivo. (tener en cuenta lo de arriba)
archivo_sin_leer = open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas.txt", encoding="UTF-8") # UTF-8 es para que caracteres como los acentos se vean bien. 
archivo_sin_leer2 = open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas.txt", encoding="UTF-8") # Solo se puede leer de una manera, por eso pongo esto.
archivo_sin_leer3 = open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas.txt", encoding="UTF-8")

print(type(archivo_sin_leer), archivo_sin_leer) # Hay que leer el archivo para obtener algo de utilidad.

print("-------------------")


# Leer líneas:

lineas = archivo_sin_leer.readlines() # Devuelve una lista con cada una de las líneas. Pone \n para marcar un salto de línea.

print(lineas)

print("-------------------")


# Leer la primera línea:

linea = archivo_sin_leer2.readline() # Si ponemos un número en el argumento, leerá esa cantidad de caracteres.

print(linea) # Deja una línea en blanco porque creo que también lee el \n, lo cual genera un salto de línea.

print("-------------------")


# Leer el archivo:

archivo = archivo_sin_leer3.read()

print(archivo) # Ahora sí que vemos lo que contiene el archivo.

print("-------------------")


# Cerrar el archivo (el que pongo como sin leer, que en realidad es el archivo):
# Es importante cerrar el archivo para evitar pérdidas de información, o errores en general.

archivo_sin_leer.close()

# archivo_sin_leer.read() Da una excepción porque no se puede leer un archivo una vez cerrado. Tendríamos que volver a abrirlo.

archivo_sin_leer = open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas.txt", encoding="UTF-8")

print(archivo_sin_leer.read()) # Ahora sí por haber vuelto a abrir el archivo.

print("-------------------")
print("-------------------")




# TRABAJAR CON ARCHIVOS TXT DE MANERA ÓPTIMA:

# Se puede trabajar con archivos como lo hemos visto anteriormente, pero esta manera es mucho más óptima en cuanto a recursos y además evita que nos olvidemos de cerrar el archivo.

# De esta manera, el archivo se abre, y además se cierra automáticamente al acabar el bloque, es decir, cuando se acaba la sangría.
with open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas.txt", encoding="UTF-8") as archivo:
    print(archivo) # Todavía no se ha leído.
    archivo_r = archivo.read()
    print(archivo_r)
# El archivo se cierra automáticamente.

print("-------------------")
print("-------------------")




# ESCRIBIR ARCHIVOS TXT:

# Al abrir un archivo con write, si este ya existe, lo SOBRESCRIBIRÁ, y si no, lo creará.
with open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas2.txt", "w", encoding="UTF-8") as archivo_escribir:
    archivo_escribir.write("Este es el texto escrito mediante Python.\nOtro texto.") # \n para hacer un salto de línea.


# Con writelines:

with open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas3.txt", "w", encoding="UTF-8") as archivo_escribir_lineas:
    archivo_escribir_lineas.writelines(["Línea 1\n", "Línea 2\n", "Línea 3"]) # Es el proceso inverso a file.readlines(). Recibe un iterable donde cada elemento es una línea. Es importante no olvidarse de \n para los saltos de línea.


# Diferencias entre write y writelines:

# Si dentro de un mismo bloque with open() ponemos dos veces writelines, no se sobrescribe, se añade.
# Por lo tanto, es muy útil para usarse dentro de un bucle.


# Con append:

# Append (a) añade texto al archivo en lugar de sobrescribir, como write (w).
with open("Apuntes\\4. Sección semi-avanzada\\4. Archivos txt\\pruebas4.txt", "a", encoding="UTF-8") as archivo_add:
    archivo_add.write("Esto no sobrescribe, añade texto.\n")
    
    # {i: archivo_add.write(f"Línea {i+1} escrita.\n") for i in range(5)} Reto de Dalto.
    # [archivo_add.write(f"Línea {i+1} escrita.\n") for i in range(5)] He estado revisando esta sección y diría que es como lo he escrito en esta línea.