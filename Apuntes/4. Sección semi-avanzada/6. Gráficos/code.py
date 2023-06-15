#---------------------------------------------------------------GRÁFICOS---------------------------------------------------------------#

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\6. Gráficos\gases.csv")

# Con esta línea de código "creamos" el gráfico.
sns.lineplot(x="Fecha", y="Gases", data=df)


# De la siguiente manera dibujo el o los puntos máximos del gráfico:

ymax = max(df["Gases"])

# Esta es la solución que me ofreció ChatGPT para obtener el valor de la columna Fecha según el valor conocido ymax.
xmax = df.loc[df['Gases'] == ymax, 'Fecha']

# Así ponemos un punto en los puntos máximos, sin importar los que hayan.
[plt.plot(x, ymax, "o") for x in xmax]


# Con esta lo mostramos.
plt.show()




# GRÁFICO DE BARRAS:
# Cofla, del curso de JavaScript, ya es programador, y tenemos que mostrar en un gráfico de barras (sectores) sus ingresos.

df_cofla = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\6. Gráficos\\ingresos_cofla.csv")
sns.barplot(x="Fuente de ingresos", y="Ingresos($)", data=df_cofla)

# Total de ingresos:
print(f"El total de ingresos de Cofla es de {sum(df_cofla['Ingresos($)'])}")

plt.show()




# GRÁFICO DE DISPERSIÓN:

df_dispersion = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\6. Gráficos\\dispersion.csv")

sns.scatterplot(x="Tiempo(unidad desconocida)",y="Dinero($)", data=df_dispersion)

plt.show()




# DIAGRAMA DE CAJAS:
# Este tipo de gráfico me parece muy curioso por toda la información que aporta, aunque tiene mucho que ver con estadística.

df_cajas = pd.read_csv("Apuntes\\4. Sección semi-avanzada\\6. Gráficos\\diagrama_de_cajas.csv")

sns.boxplot(x="Categoria", y="Valor", data=df_cajas)

plt.show()