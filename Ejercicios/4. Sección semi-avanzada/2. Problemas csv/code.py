import pandas as pd

# PROBLEMA 1:
# Cambiar el tipo de dato de una columna.

df = pd.read_csv("Ejercicios\\4. Sección semi-avanzada\\2. Problemas csv\\prueba_csv.csv")


i = 0
while i < df.shape[0]:
    df.loc[i,"Apellido"] = [df.loc[i,"Apellido"]]
    i+=1
print(df)

print("---------------")
print("---------------")



# PROBLEMA 2:
# Eliminar filas duplicadas.

df2 = pd.read_csv("Ejercicios\\4. Sección semi-avanzada\\2. Problemas csv\\prueba_csv.csv")

# Lamentablemente, no se me ocurre como resolver este problema.

# Solución de Dalto:
df2 = df2.drop_duplicates()
print(df2)