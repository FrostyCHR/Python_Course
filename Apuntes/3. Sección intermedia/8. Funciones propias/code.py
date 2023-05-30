#---------------------------------------------------------------FUNCIONES PROPIAS---------------------------------------------------------------#

# Función extremadamente simple.
def saludar1():
    print("Hola, Dalto. ¿Como se encuentra el día de hoy, amable caballero?")

saludar1() # ¿Y si la persona no se llama Dalto?


# Función con parámetros. ("variables" que toman un valor a la hora de ejecutar el código)
def saludar2(nombre):
    print(f"Hola, {nombre}. ¿Como se encuentra el día de hoy, amable caballero?")

saludar2("Pedro")
saludar2("Ana") # ¿Y si la persona es mujer?


def saludar3(nombre, genero):
    if genero.lower() == "hombre":
        adjetivo = "caballero"
    elif genero.lower() == "mujer":
        adjetivo = "dama"
    else:
        adjetivo = "persona"
    
    print(f"Hola, {nombre}. ¿Como se encuentra el día de hoy, amable {adjetivo}?")

saludar3("Fernando", "HOMBRE")
saludar3("Laura", "mujer")
saludar3("Alex", "homre")




# Función con return. (ahora la llamada a la función es igual a lo que devolvemos)
def ec_grado_2(a,b,c):
    x1 = (-b + ((b**2 - 4 * a * c) ** (1/2))) / (2 * a)
    x2 = (-b - ((b**2 - 4 * a * c) ** (1/2))) / (2 * a)
    return x1, x2

x1, x2 = ec_grado_2(1,-2,-3) # Gracias a return, podemos usar datos de una función fuera de ella. # Usando desempaquetado.

print(f"x1 = {x1}; x2 = {x2}")




# Función con un número indefinido de argumentos. (parámetro rest en JS)
# Debe ser el último argumento de la función.

def suma(otro_parámetro, *nums): # Parámetro args.
    return otro_parámetro,sum(nums)

print(suma("Hola",1,5,53,0,53,9,9023,2))

# Operador args: (igual que spread en JS)

lista1 = [15,False, "Hola", 1.5]
lista2 = [True, "Si"]

lista3 = [*lista1,*lista2]

print(lista3)

# Pasar una lista / tupla como argumento de una función con varios parámetros:

ec_grado_2(*(1,5,-2))




# Función con argumentos desordenados:

def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres {adjetivo}."

# Probamos a ponerlo desordenado. Si no ponemos nada, se pone el valor por defecto del parámetro.
print(frase("Dalto", "Lucas",))

# Al hacerlo así, aunque esté desordenado funciona bien. (keyword arguments). Además, estamos poniendóle valor a adjetivo.
print(frase(adjetivo="maquinola", apellido="Dalto", nombre="Lucas"))