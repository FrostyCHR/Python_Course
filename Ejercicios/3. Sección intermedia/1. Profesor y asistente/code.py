# Obtenemos la cantidad de alumnos.

cantidad_alumnos = input("¿Cuántos alumnos han venido a clase?: ")

while cantidad_alumnos.isnumeric() == False:
    print("Introduce un numero entero.")
    cantidad_alumnos = input("¿Cuántos alumnos han venido a clase?: ")
    
cantidad_alumnos = int(cantidad_alumnos)


alumnos = []
contador = 1

# Obtenemos una lista con otras listas dentro correspondientes a cada alumno.

while contador <= cantidad_alumnos:
    
    nombre = input(f"¿Cuál es el nombre del alumno {contador}?: ")
    edad = input(f"¿Cuál es la edad de {nombre}?: ")
    
    # Comprobamos que es un entero.
    
    while edad.isnumeric() == False:
        print("Introduce un numero entero.")
        edad = input(f"¿Cuál es la edad de {nombre}?: ")
    
    edad = int(edad)
    alumno = [nombre, edad]
    alumnos.append(alumno)

    # Mi idea era hacer alumnos[edad] = alumno, pero no funciona debido a que si hubiera más de un alumno con la misma edad, se sobrescribiría.
    
    contador += 1

# (Con ayuda de IA ordenamos la lista):
alumnos.sort(key=lambda data: data[1])

# Ordenamos la información.
print(f"El profesor es {alumnos[-1][0]} y su asistente es {alumnos[0][0]}.")