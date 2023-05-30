numero = input("Introduce un numero para generar todos los primos hasta llegar a él: ")

while numero.isnumeric() == False:
    numero = input("Introduce un numero para generar todos los primos hasta llegar a él: ")
    
numero = int(numero)

def primos(numero_objetivo):
    
    numero = 2

    numeros_primos = []
    
    # Un bucle para ir cambiando de numero.
    while numero <= numero_objetivo:
        divisor = 2
        
        # Otro bucle para comprobar si es primo o no.
        while numero % divisor != 0:
            divisor += 1
            if divisor == numero:
                numeros_primos.append(numero)
                break
        numero += 1
    
    # Por la manera en la que está hecho, no da el 2. Lo arreglamos con este fix.
    if numero >= 2:
        numeros_primos.insert(0, 2)
    
    # Retornamos la lista.
    return numeros_primos

print(primos(numero))