#---------------------------------------------------------------TIPOS DE DATOS COMPUESTOS---------------------------------------------------------------#

# Los tipos de datos compuestos incluyen uno o más datos simples.




# List: (lista, array)
# Se usan []. Se puede modificar totalmente y parcialmente. Funciona con orden e índices, como en JavaScript.

lista = ["Hola", 2, "Adiós"]
lista[2] = "Hola de nuevo"

print(lista[0])
print(lista)



# Tuple: (tupla)
# Se usan (). Se puede modificar totalmente.

tupla = ("Buenos días", True, 5)
# tupla[0] = "No" No funciona.

print(tupla[0])
print(tupla)



# Set: (conjunto)
# Se usan {}. Se puede modificar totalmente. NO funciona con índices. Los objetos no tienen un orden fijo. No admite datos duplicados.

conjunto = {"¿Cómo estás?", False, 123}
# conjunto = {"Si"} Funcionaría.

print(conjunto)
# print(conjunto[0]) No funciona.



# Dictionary: (diccionario, objetos JSON en JS)
# Se usan {} en varias líneas. Sitaxis similar a los JSON en JS.

diccionario = {
    "Nombre": "Lucas",
    "Apellido": "Dalto",
    "Edad": 24,
    "País": "Argentina"
}

print(diccionario)
print(diccionario["Apellido"])