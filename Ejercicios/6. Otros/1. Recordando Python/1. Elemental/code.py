# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


def barras():
    return input("¿Cuántas barras que no son del día se han vendido? ")

while True:
    try:
        nbarras = int(barras())
    except:
        print("Introduce un numero entero.")
    else:
        break

precio_barra = 3.49
descuento_barra_no_dia = 60

print(f"El precio habitual de una barra de pan es {precio_barra}€.\nEl descuento de las barras que no son frescas es de un {60}%.\nEl precio de todas las barras que no son frescas es de {round(precio_barra*nbarras*(100 - descuento_barra_no_dia)/100, 2)}€.")