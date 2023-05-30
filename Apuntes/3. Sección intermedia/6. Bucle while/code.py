#---------------------------------------------------------------BUCLE WHILE---------------------------------------------------------------#

# Como en otros lenguajes, while repite el mismo código siempre y cuando una condición sea verdadera (True). La diferencia con for es que for sirve para recorrer / iterar elementos, mientras que while solo repite trozos de código. Si no se tiene cuidado, se puede llegar a bucles infinitos.

contador = 0

# La condición se verifica al iniciar cada vuelta. En este caso, se ejecutará 5 veces.
while contador < 5:
    print(contador)
    contador += 1 # contador++ no funciona en Python.