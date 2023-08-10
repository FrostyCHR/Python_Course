# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def numasignaturas():
    return input("¿Cuántas asignaturas tienes? ")

while True:
    try:
        nasignaturas = int(numasignaturas())
    except:
        print("Introduce un numero entero.")
    else:
        break

asignaturas = []

def notas():
    return input(f"¿Qué nota has sacado? ")

contador = 0
while contador < nasignaturas:
    asignatura = input(f"¿Cuál es la asignatura {contador+1}? ")
    
    while True:
        try:
            nota = float(notas())
        except:
            print("Introduce un numero entero.")
        else:
            break
    
    if nota <= 5:
        asignaturas.append([asignatura, nota])
    
    contador +=1

print(f"Debes recuperar las siguientes asignaturas: {asignaturas}")