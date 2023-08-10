#---------------------------------------------------------------ARCHIVOS CSV---------------------------------------------------------------#

# CSV significa "Comma separated values". Es muy útil en el análisis de datos.

# Se puede trabajar con este módulo, pero existe otro llamado Pandas que es mejor y se usa más en proyectos. Lo veremos más adelante.
import csv

with open("Apuntes\\4. Sección semi-avanzada\\5. Archivos CSV\\prueba_csv.csv") as archivo:
    #print(archivo.read()) # Lo lee como un txt normal. (Tengo que comentarlo o si no no funciona el for)
    reader = csv.reader(archivo)
    print(reader) # Esto es un objeto csv reader, el cual es iterable.
    print("---------------")
    
    for row in reader:
        print(row)
    print("---------------")
    print("---------------")



# CSV CON PANDAS:

import pandas as pd # Está estandarizado usar pandas como pd. (Hay que instalarlo)

df = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\5. Archivos CSV\\prueba_csv.csv")
# df significa dataframe, y es una estructura de datos que podemos entender como similar a una hoja de cálculo.
print(df)

df2 = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\5. Archivos CSV\\prueba_csv.csv")

print("---------------")

# Obteniendo una columna:
print(df["Edad"])

print("---------------")


# Ordenar csv:

df_ordenado_ascendiente = df.sort_values("Edad")
df_ordenado_descendiente = df.sort_values("Edad", ascending=False)

df_orden_letras = df.sort_values("Apellido")

print(df_ordenado_ascendiente)
print("")
print(df_ordenado_descendiente)
print("")
print(df_orden_letras)

print("---------------")


# Concatenar dos csv:

df_concatenado = pd.concat([df,df2])
print(df_concatenado)
# Importante ver que el índice (numero a la izquierda) se mantiene igual al concatenar, es decir, los índices se repiten.

print("---------------")

# sort_index() ordena un dataframe segun los índices.
df_concatenado = df_concatenado.sort_index()

print(df_concatenado)

print("---------------")


# Obtener un número concreto de filas:

# head(): Obtiene un numero concreto de filas desde arriba.

# Nos sale información diferente si no cogemos ninguna fila.
print(df.head(0))
print("")
print(df.head(2))

# tail(): Igual que head, pero desde abajo.

print("")
print(df.tail(1))

print("---------------")


# Obtener numero de filas y de columnas:

# shape: Es una propiedad (descripción de un objeto, como una variable) de dataframes que devuelve una tupla con la cantidad de filas y de columnas. La columna con los índices y la fila con el encabezado no cuentan.

filas_y_columnas = df.shape

# Con desempaquetado:
filas,columnas = df.shape

print(f"El numero de filas es {filas_y_columnas[0]}, y el numero de columnas es {filas_y_columnas[1]}.")

print("---------------")


# Obtener valores estadísticos de un dataframe:

# describe(): Devuelve otro dataframe con diversa información relacionada a la estadística como los cuartiles o la media.

print(df.describe())

print("---------------")
print("---------------")



# SLICING:
# Este concepto está un poco fuera de lugar en esta sección del curso, pero es muy importante al trabajar con pandas. Es similar al método .slice() de JS.
# Aunque en este ejemplo lo use en listas, también sirve en strings. (tuplas no, porque no se pueden modificar, y sets tampoco porque no tienen orden)

lista = [0,512,62,"Hola", False]

# El primer número es el índice en el que empezamos (incluido), y el segundo es en el que acabamos (no incluido). Nos referimos a LOS ELEMENTOS QUE NOS QUEDAMOS, el resto se eliminan.
lista_cortada1 = lista[-3:-1]
lista_cortada2 = lista[1:3]
lista_cortada3 = lista[3:]

print(lista_cortada1, lista_cortada2, lista_cortada3, lista) # La lista no se modifica.

print("---------------")



# Valores específicos:

# loc: Hay que poner una lista donde el primer elemento es el índice de la fila y el segundo es el nombre de la columna.

# iloc: Es similar al anterior, pero la columna también funciona con índices. (iloc --> index loc)

fila_1_columna_nombre = df.loc[1,"Nombre"]
fila_1_columna_0 = df.iloc[1,0]

print(fila_1_columna_nombre, fila_1_columna_0) # He accedido a lo mismo con ambas propiedades.

print("---------------")

# Mezclando esto con slicing:

toda_la_columna_edad_loc = df.loc[:,"Edad"]
toda_la_columna_edad_sin_loc = df["Edad"]

print(toda_la_columna_edad_loc)
print("")
print(toda_la_columna_edad_sin_loc)
# Ambas maneras dan el mismo resultado.

print("---------------")

toda_la_fila_1_loc = df.loc[1,:]
# toda_la_fila_1_sin_loc = df[1] Para las filas esto no funciona.

print(toda_la_fila_1_loc)