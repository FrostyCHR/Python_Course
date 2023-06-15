#---------------------------------------------------------------ENRUTAMIENTO DE MÓDULOS---------------------------------------------------------------#

# (Module routing) Consiste en acceder a módulos que no se encuentran en la misma carpeta que el principal (desde el que llamamos).


# Si el módulo está "más al fondo" en la ruta:
import funciones.funciones_mat

# Si el módulo está atrás:
import sys

print(sys.path) # Todas las rutas donde hay módulos.

# Añadimos la ruta deseada.
sys.path.append("C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\\Apuntes\\4. Sección semi-avanzada\\1. Módulos")

import modulo as m_otra_carpeta_anterior # Por algún motivo, no lo marca como correcto, pero funciona.


# Todos los módulos built-in.
print(sys.builtin_module_names)



# Se debe llamar así, siempre y cuando no usemos as.
print(funciones.funciones_mat.por2(2))

print(m_otra_carpeta_anterior.sqrt(25))