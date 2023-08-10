# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

def create_mult(n):
    with open(f"C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\Ejercicios\\6. Otros\\1. Recordando Python\\4. Semi-avanzado\\1. TXT\\tabla-{n}.txt", "w", encoding="UTF-8") as file:
        for i in range(11):
            file.write(f"{n}*{i} = {n*i}\n")

numero_create = input("Escribe un número para crear su tabla: ")

while numero_create.isnumeric() == False:
    numero_create = input("Escribe un número para crear su tabla: ")

create_mult(int(numero_create))



# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def find_mult(n):
    try:
        with open(f"C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\Ejercicios\\6. Otros\\1. Recordando Python\\4. Semi-avanzado\\1. TXT\\tabla-{n}.txt", encoding="UTF-8") as file:
            print(file.read())
    except:
        print("Todavía no existe la tabla seleccionada. Créala antes.")

numero_find = input("Escribe un número para ver su tabla: ")

while numero_find.isnumeric() == False:
    numero_find = input("Escribe un número para ver su tabla: ")

find_mult(int(numero_find))



# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def find_mult_e(n,m):
    try:
        with open(f"C:\\Users\\PC Master Race\\OneDrive\\Escritorio\\Desarrollo de Software\\Python\Ejercicios\\6. Otros\\1. Recordando Python\\4. Semi-avanzado\\1. TXT\\tabla-{n}.txt", encoding="UTF-8") as file:
            print(file.readlines()[m])
    except:
        print("Todavía no existe la tabla seleccionada. Créala antes.")

numero_t = input("Escribe un número para ver su tabla: ")

while numero_t.isnumeric() == False:
    numero_t = input("Escribe un número para ver su tabla: ")


numero_m = input("Escribe un numero para ver esa fila concreta (0-10): ")

while numero_m.isnumeric() == False:
    numero_m = input("Escribe un numero para ver esa fila concreta (0-10): ")

while True:
    if int(numero_m) > 10:
        print("Te has pasado de 10, vuelve a intentarlo.")
        break
    else:
        find_mult_e(int(numero_t), int(numero_m))
        break