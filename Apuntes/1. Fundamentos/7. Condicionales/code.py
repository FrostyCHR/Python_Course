#---------------------------------------------------------------CONDICIONALES---------------------------------------------------------------#

# Son tan simples como en cualquier otro lenguaje. Si la condición se cumple, ejecuta algo, si no, ejecuta otra cosa. Lo único curioso es la sintaxis.


# IF - ELSE:

edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
    # Forma parte del if.
else:
    print("Eres menor de edad.")
    # Forma parte del else.

# No forma parte de ningún bloque.




# Varios IF:
# Puede "entrar" en varios.

seguidores = 10000

# Esto no sería correcto, ya que se ejecutarían varios if en casi todos los casos.
if seguidores >= 10000000:
    print("Te conocen hasta en el polo norte.")

if seguidores >= 1000000:
    print("Te conoce todo tu país.")

if seguidores >= 1000:
    print("Te conoce tu barrio.")

if seguidores >= 10:
    print("¿Acaso te conoce tu familia?")




# ELSE - IF: (elif)
# Solamente "entra" en un bloque if.

money = 1000

# Si se cumplen varias, solamente entra en la primera.
if money >= 10000:
    print("Muy bien en cuanto a dinero.")
    
elif money >= 1000:
    print("Nada mal para ser joven.")