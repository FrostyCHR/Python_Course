#---------------------------------------------------------------MÓDULOS---------------------------------------------------------------#

# Un módulo en Python es un archivo .py. Por lo tanto, sí, este archivo es un módulo. Los módulos contienen código, principalmente funciones, pero también objetos, strings, listas, lo que queramos. Hay tres tipos de módulos:
# - Python modules: Módulos "por defecto" de Python creados en C++.
# - Own modules: Módulos creados por ti o por tu empresa.
# - "Third-party" modules: Módulos creados por personas ajenas.

# IMPORTANTE: No tener una función y una variable con el mismo nombre, ya que no nos importaría lo que queremos. Para evitarlo, se puede poner la primera letra de las funciones en mayúscula.

# Al usar módulos se crea automáticamente una carpeta llamada __pycache__. Hay que ignorarla, ya que hace que este proceso funcione mejor y más rápido.


# Solamente el nombre, sin el .py. Conocido como namespace.
import modulo 

# As lo que hace es asignarle un nombre diferente al mismo módulo en este archivo.
import saludo as greeting 

# Con from xxxx import xxxx solamente importamos un elemento del módulo. Se puede mezclar con as.
from saludo import saludo_a_Dalto as s_Dalto, lista_sin_sentido as li_sn # Con la coma importamos otra cosa del mismo módulo (se puede mezclar con as).


print(type(modulo))

print(modulo.sqrt(4)) # Las funciones dentro del módulo son métodos, y el módulo es el objeto.

print(greeting.saludo("Pedro"))

# Con variables:
print(s_Dalto)
print(li_sn)



# Accediendo al nombre del módulo:
print(__name__)

# Otro módulo:
print(greeting.__name__) # Da el nombre verdadero, no el que asignamos con as.