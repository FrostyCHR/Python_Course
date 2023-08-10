#---------------------------------------------------------------EXCEPCIONES---------------------------------------------------------------#

# Una excepción es un error que ocurre en un programa y que provoca el fin de la ejecución. En esta sección vamos a aprender a manejarlas.

# Esta función multiplica todos los números que pongamos como argumentos debido a args (*), pero no funciona al poner otros tipos de datos.

def multiplicar(*nums):
    resultado = 1
    for num in nums:
        resultado = resultado*int(num)
    return resultado

print(multiplicar(2,3,2))


# Con try y except, junto con un bucle "infinito", logramos hacer que en caso de haber una excepción, no se pare el programa y que te vuelva a pedir los números.

while True:
    try:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        c = input("Numero 3: ")
        d = input("Numero 4: ")
        print(multiplicar(a,b,c,d))
    except Exception as e: # Igual que catch en JS, pero aquí sí que pongo e porque no lo confundo con e de event.
        print("Introduce números enteros.")
        print(f"Error: {e}. \n Tipo: {type(e).__name__}")
    else: # Esto funciona similar al else en for. Si try va bien, se ejecuta. Si hay una excepción, no.
        break
    finally: # No se suele usar demasiado.
        print("Esto SIEMPRE se ejecuta, aunque haya un break antes en el else.")

# Se pueden usar diversos except. Hay muchos tipos de excepciones, como ZeroDivisionError.

print("------------------")



# CREANDO UNA PROPIA EXCEPCIÓN:

# Para esto hace falta aplicar POO (programación orientada a objetos). En el momento en el que estudio esta parte (6-2023), todavía no controlo esta manera de programar en este lenguaje, por lo que lo he copiado del curso.

# Raise es la palabra clave para lanzar excepciones manualmente, similar a throw en JS.

class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Error creado por el desarrollador: {err}")

try:
    raise MiExcepcion("Error cualquiera.") # Esto muestra datos por consola debido al print de la clase.
except Exception as e:
    print(type(e).__name__)

raise MiExcepcion("Error cualquiera.")