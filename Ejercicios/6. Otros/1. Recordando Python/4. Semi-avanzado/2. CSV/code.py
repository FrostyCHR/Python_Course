# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:


import pandas as pd


# Generar un DataFrame con los datos del fichero.

df = pd.read_csv("C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\\Ejercicios\\6. Otros\\1. Recordando Python\\4. Semi-avanzado\\2. CSV\\titanic.csv")

print(df)


# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.

rows,columns = df.shape

print(f"{rows} filas y {columns} columnas. {rows*columns} datos.")
print("--------------")
print(df.columns)
print("--------------")

# Mi solución.
[print(type(df[i][0])) for i in df.columns]
print("--------------")
# Versión de la web.
print(df.dtypes)
print("--------------")

print(df.head(10))
print("--------------")
print(df.tail(10))
print("--------------")


# Mostrar por pantalla los datos del pasajero con identificador 148.

print(df.loc[df["PassengerId"] == 148,:]) # Gracias a ChatGPT.
print("--------------")


# Mostrar por pantalla las filas pares del DataFrame.

print(df.loc[df.index%2 == 0,:])
print("--------------")


# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.

orden = df.sort_values("Name")

first_class = orden.loc[orden["Pclass"] == 1,"Name"]

print(first_class)
print("--------------")


# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.

nsurvive = len(df.loc[df["Survived"] == 1,"Survived"])
ndead = len(df.loc[df["Survived"] == 0,"Survived"])

print(f"Sobrevivió un {(nsurvive/(nsurvive+ndead))*100}% y murió un {(ndead/(nsurvive+ndead))*100}%.")
print("--------------")


# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

for i in range(3):
    nclass = orden.loc[orden["Pclass"] == i+1,:]
    
    nsurviven = len(nclass.loc[nclass["Survived"] == 1,"Survived"])
    ndeadn = len(nclass.loc[nclass["Survived"] == 0,"Survived"])
    
    print(f"En la {i+1} clase sobrevivió un {(nsurviven/(nsurviven+ndeadn))*100}% y murió un {(ndeadn/(nsurviven+ndeadn))*100}%.")

print("--------------")


# Eliminar del DataFrame los pasajeros con edad desconocida.

k_age = df.loc[df["Age"] > 0,:] # Como no sé cómo detectar cuando no sabemos la edad, detecto cuando sí que la sabemos.

print(k_age)
print("--------------")


# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

for i in range(3):
    nclass = orden.loc[orden["Pclass"] == i+1,:]
    female = nclass.loc[nclass["Sex"] == "female","Age"]
    
    print(f"La media de edad de las mujeres de la clase {i+1} es de {female.describe()['mean']} años.")

print("--------------")


# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.

values_new_column = []

for i in range(len(k_age)):
    if k_age.iloc[i,5] < 18:
        values_new_column.append(True)
    else:
        values_new_column.append(False)

k_age["Minor"] = values_new_column # Solución de ChatGPT.
print(k_age)

k_age.to_csv("C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\\Ejercicios\\6. Otros\\1. Recordando Python\\4. Semi-avanzado\\2. CSV\\titanic_after.csv")


# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.

is_minor = [False, True]

for yes_no in is_minor:
    df_yes_no = k_age.loc[k_age["Minor"] == yes_no,:]
    for i in range(3):
        nclass_yes_no = df_yes_no.loc[df_yes_no["Pclass"] == i+1,:]
    
        nsurviven = len(nclass_yes_no.loc[nclass_yes_no["Survived"] == 1,"Survived"])
        ndeadn = len(nclass_yes_no.loc[nclass_yes_no["Survived"] == 0,"Survived"])

        if yes_no == False:
            print(f"En la {i+1} clase sobrevivió un {(nsurviven/(nsurviven+ndeadn))*100}% de mayores de edad y murió un {(ndeadn/(nsurviven+ndeadn))*100}%.")
        else:
            print(f"En la {i+1} clase sobrevivió un {(nsurviven/(nsurviven+ndeadn))*100}% de menores de edad y murió un {(ndeadn/(nsurviven+ndeadn))*100}%.")