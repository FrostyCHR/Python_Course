# VARIABLES:

# Palabras por segundo

pps_normal = 2
pps_dalto = 2*130/100

texto_usuario = input("Introduce un texto real (o no). ")



# A:

print("---------------------------------")

numero_palabras = len(texto_usuario.split(" "))

tiempo_normal = numero_palabras*100 // pps_normal / 100

print(f"Has escrito {numero_palabras} palabras.")
print(f"Tardarías {tiempo_normal} segundos en decir el texto.")



# B:

if tiempo_normal > 60:
    print("---------------------------------")
    print("Pará flaco, no te pedí un testamento.")



# C:

print("---------------------------------")

tiempo_dalto = numero_palabras*100 // pps_dalto / 100

print(f"Dalto tardaría {tiempo_dalto} segundos en decir el texto.")