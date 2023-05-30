#---------------------------------------------------------------DESEMPAQUETADO---------------------------------------------------------------#

# Es una técnica de creación de variables en Python (y otros lenguajes) que consiste en asignar los valores de las nuevas variables respecto a un dato compuesto.


# Con tuplas:

tuple1 = ("Lucas", "Dalto", 1000000)

nombre,apellido,suscriptores = tuple1

print(nombre,apellido,suscriptores)


# Con listas:

list1 = [4, "ESO", "B", 27]

curso,estudios,clase,alumnos = list1

print(curso,estudios,clase,alumnos)


# Con sets:

set1 = {"Joker","Panther","Queen","Crow"}

attacker1,attacker2,support1,support2 = set1

print(attacker1,attacker2,support1,support2) # No sirve de mucho, ya que toma un orden aleatorio cada vez.