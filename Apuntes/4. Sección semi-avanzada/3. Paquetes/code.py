#---------------------------------------------------------------PAQUETES---------------------------------------------------------------#

# Un paquete es una carpeta que contiene diversos módulos. Para que Python entienda que es un paquete, dentro debe haber un archivo __init__.py, aunque esté vacío. Si no estuviera, se entendería como carpeta normal.

# Un subpaquete es un paquete dentro de otro paquete.


# A la hora de importar, los paquetes tienen prioridad a los módulos sueltos al tener el mismo nombre.

import Package.modulo # No se puede decir import Package, por lo tanto para evitar largas líneas de código es mejor usar lo siguiente:
from Package import saludo

print(type(Package))
print(Package.modulo.sqrt(4))
print(saludo.saludo_a_Dalto)