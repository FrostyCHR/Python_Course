# Pedimos el numero y nos aseguramos de que sea un numero.

numero = input("Introduce un numero para generar todos los numeros de la secuencia de Fibonacci hasta él: ")

while numero.isnumeric() == False:
    numero = input("Introduce un numero para generar todos los numeros de la secuencia de Fibonacci hasta él: ")
    
numero = int(numero)

# Función para conseguir la secuencia.

def fibonacci_hasta(numero_hasta):
    fibonacci = [0, 1]
    
    while True:
        
        # Sumamos los 2 numeros anteriores en la secuencia.
        numero = fibonacci[-2] + fibonacci[-1]
        
        # Al pasarse del límite, acabamos el bucle.
        if numero > numero_hasta:
            break
        
        fibonacci.append(numero)
    
    return fibonacci
    
print(fibonacci_hasta(numero))