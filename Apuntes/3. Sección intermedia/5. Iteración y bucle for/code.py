#---------------------------------------------------------------ITERACIÓN Y BUCLE FOR---------------------------------------------------------------#

# Iterar (repeat en inglés) es repetir la misma sección de código diversas veces, pero en cada ocasión, una variable toma un valor diferente.
# Para iterar, se usa for in, que es igual a for of en JS.

# En Python, no existe el típico bucle for: [for (let i = 0; i < 5; i++) (5 veces)]. Existe for in.




# ITERAR LISTAS Y TUPLAS:


animales = ["Perro", "Gato", "Gorila", "Pájaro", "Estudiante de 3ro de la ESO"]
numeros = (2,521.243,-24.5,0,-5)
ordenes = ["Amanecer Dorado", "Toros Negros", "Mantis Verdes", "Águilas Plateadas", "Leones Carmesíes"]

for animal in animales:
    print(f"La variable animal es igual a {animal}.")

print("------------------------")



# ¿Cómo iterar dos listas a la vez? (o más) (zip)
# Deben tener el mismo número de elementos.

for animal,numero,orden in zip(animales, numeros, ordenes):
    print(f"Ahora animal vale {animal}.")
    print(f"Pero número tambien vale {numero}.")
    print(f"Ahora la orden de Black Clover es {orden}.")

print("------------------------")



# Iterar con range:
# Dos parámetros hacen que la variable empieze en el primero y acabe en el segundo (sin contarlo, números).

for num in range(5,10):
    print(num)
print("------------------------")

# Un único parámetro hace que vaya de 0 hasta el número.

for num in range(5):
    print(num)
print("------------------------")

# Manera no óptima:

for index in range(len(animales)):
    print(animales[index])
print("------------------------")



# Iterar con índice (enumerate):

for element in enumerate(animales):
    print(element, type(element)) # Element es una tupla cuyo primer elemento es el índice y el segundo es el elemento en sí.
    index = element[0]
    value = element[1]
    print(f"El índice es {index} y el valor es {value}.")

print("------------------------")

# Mejor manera de hacer lo anterior:

for index,value in enumerate(ordenes):
    print(index, value)

print("------------------------")



# Usar else con for in:
# Else se ejecuta al acabar el bucle (incluso si el bucle no se ejecuta nunca).

for num in numeros:
    print(f"El número es {num}.")
else:
    print("El bucle ha acabado.")

print("------------------------")
print("------------------------")




# ITERAR SETS:


carreras = {"Medicina", "Física", "Ing. Informática", "Ing. Civil", "Derecho", "ADE"}

for index,carrera in enumerate(carreras):
    print(f"El ¿índice? es {index} y el valor es {carrera}.")
    # Por algún motivo, el "índice" funciona, pero no sirve de nada ya que cada vez que se ejecuta toma un "orden" diferente.

print("------------------------")
print("------------------------")




# ITERAR DICCIONARIOS:


dalto = dict(nombre="Lucas", apellido="Dalto", suscriptores=664000)

for key in dalto:
    print(f"La variable key vale {key}.")

print("------------------------")

for key,value in dalto.items():
    print(f"La key es {key}, cuyo valor es {value}.")

print("------------------------")
print("------------------------")




# OTRAS ITERACIONES:


# Continue: Se salta todo lo que queda de esa iteración y pasa a la siguiente.
# Break: Para el bucle.

frutas = ["manzana", "kiwi", "pera", "piña", "uva", "naranja", "nectarina", "mandarina", "sandía", "paraguayo"]

for fruta in frutas:
    if fruta == "kiwi" or fruta == "naranja":
        continue
    if fruta == "sandía":
        break
    print(f"Me voy a comer un/una {fruta}.") # Podemos poner un if para evitar el un/una.
else:
    print("Se ha acabado el bucle.")
# Aquí se ve el uso de else después de for, ya que no se ejecuta en caso de haber un break.

print("------------------------")



# Iterar strings:

string = "Hola, ¿cómo estás?"

for caracter in string:
    print(caracter)

print("------------------------")



# for en una sola línea de código:

numeros = [2, 5, 6.4, -25.5, 0, -1.4, -5]

numeros_duplicados = [x*2 for x in numeros] # x*2 se puede sustituir por otra operación matemática.

print(numeros_duplicados)