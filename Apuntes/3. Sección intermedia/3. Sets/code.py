#---------------------------------------------------------------SETS---------------------------------------------------------------#

# Un set, como ya hemos visto, es un tipo de dato compuesto en el que sus elementos no tienen un orden concreto. Se crea con {}. No puede contener listas dentro, pero tuplas sí ya que no son modificables.

set1 = {"elemento1",2, True}


# Función set:
# Crea un set a partir de una lista o de una tupla.

set2 = set(("elemento en posición 0", 1))

# Cómo meter conjuntos dentro de otros conjuntos:
# De manera normal, no se puede, ya que lanza una excepción. Pero se puede hacer mediante otra función frozenset.

set_interior = frozenset({"1",8,"2pik"}) # Es similar a set, pero se puede poner dentro de otros. (acepta tuplas y listas)
set3 = {set_interior, "Hola", False}

print(set3)




# TEORÍA DE CONJUNTOS:
# Esta teoría indica que si tenemos un conjunto cualquiera, y otro con ÚNICAMENTE algunos de los datos del anterior, el primer conjunto es un superconjunto (respecto al segundo), y el segundo es un subconjunto (respecto al primero).

setA = {1,2,3,"hola"}
setB = {3,"hola"}
setC = {4,"adiós"}


# Estas comprobaciones se pueden hacer también así:
# set1.issuperset(set2) = set1 > set2
# set1.issubset(set2) = set1 <= set2

resultado1 = setA.issuperset(setB) # True.
resultado2 = setB.issubset(setA) # True.
resultado3 = setB.issuperset(setA) # False.

# isdisjoint() comprueba si un conjunto no comparte nada con otro. En caso afirmativo, True, y en caso negativo, False.

resultado4 = setA.isdisjoint(setC) # True.
resultado5 = setA.isdisjoint(setB) # False.

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)