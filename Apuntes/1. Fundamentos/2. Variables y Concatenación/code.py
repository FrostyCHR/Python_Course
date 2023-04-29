#---------------------------------------------------------------VARIABLES Y CONCATENACIÓN---------------------------------------------------------------#

# Al igual que en otros lenguajes, las variables son un espacio en la memoria con un nombre dedicadas a guardar datos. Se puede cambiar su valor.
# Como principal diferencia, en Python no hace falta usar ningún tipo de palabra clave para crearlas como let, int o var (ni poner punto y coma ;).


n1 = 54
n2 = 2
suma = n1 + n2
print(suma)

# del borra una variable, como si nunca hubiese existido a partir de esa línea de código.
del suma



# Hay diversas maneras de concatenar (unir varios strings) en Python:

# Manera 1 (no funciona con otros datos que no sean strings)

nombre = "Jorge"
saludo = "Hola " + nombre

print(saludo)


# Manera 2
# f string: Es un tipo de string que permite la concatenación de una manera MUY cómoda. Son el equivalente a los template strings en JavaScript.


nombre = 6
saludo = f"Hola {nombre}"

print(saludo)



# Operadores de pertenencia:
# in: Se pregunta si algo se encuentra en otra cosa. Devuelve True o False.
# not in: Se pregunta si algo NO se encuentra en otra cosa. Lo contrario al anterior.

print("Si" in "Si es así...")
print("Si" not in "Si es así...")