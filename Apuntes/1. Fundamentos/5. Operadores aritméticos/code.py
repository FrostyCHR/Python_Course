#---------------------------------------------------------------OPERADORES ARITMÉTICOS---------------------------------------------------------------#

# Estos operadores nos permiten hacer cálculos matemáticos simples.

a = 10
b = 6


# Suma:

suma = a + b
print(suma)

# Resta:

resta = a - b
print(resta)

# Multiplicación:

multiplicacion = a * b
print(multiplicacion)

# División:

division = a / b
print(division) # Devuelve SIEMPRE un float, aunque el resultado sea entero.

# Exponencialización:

exponencialización = a ** b
print(exponencialización)

# División baja:

division_baja = a // b
print(division_baja) # Devuelve un integer (truncando, eliminando los decimales).

# Residuo:

residuo = a % b
print(residuo)



# Type:

tipo_de_dato = type(division) # Igula que typeof en JS, pero como función.
print(tipo_de_dato)