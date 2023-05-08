# Variables:

# Cursos en general:
cursos_generales_minimo = 2.5
cursos_generales_media = 4
cursos_generales_maximo = 7

cursos_generales_crudo = 5

# Cuso de Dalto:
curso_dalto = 1.5

curso_dalto_crudo = 3.5

print("----------------------------------------------------------------")


# A:

dalto_vs_min = 100 - curso_dalto/cursos_generales_minimo*100
# El de Dalto dura lo mismo que el 60% del general más corto.

dalto_vs_med = 100 - curso_dalto/cursos_generales_media*100

dalto_vs_max = 100 - curso_dalto*1000//cursos_generales_maximo/10 # Esto es un TRUCAZO para truncar más o menos bien. *1000 / 10 = *100, pero al hacerlo de esa manera, la división baja lo trunca, dejándolo sin decimales, pero al dividirlo entre diez se nos queda una cifra. Para tener más, podemos hacer *10000 / 100, *100000 / 1000...

print(f"El curso de Dalto es un {dalto_vs_min}% más rápido que el general más rápido.")
print(f"El curso de Dalto es un {dalto_vs_med}% más rápido que la media de los generales.")
print(f"El curso de Dalto es un {dalto_vs_max}% más rápido que el general más lento.")

print("----------------------------------------------------------------")



# B:

por_red_media = 100 - cursos_generales_media/cursos_generales_crudo*100
por_red_dalto = 100 - curso_dalto*1000//curso_dalto_crudo/10

print(f"En los cursos estándar se ha reducido un {por_red_media}% de material.")
print(f"En el curso de Dalto se ha reducido un {por_red_dalto}% de material.")

print("----------------------------------------------------------------")



# C:

media_entre_dalto = cursos_generales_media*100//curso_dalto/100
dalto_entre_media = curso_dalto/cursos_generales_media

print(f"Ver 10 horas del curso de Dalto equivalen a {media_entre_dalto*10} horas de un curso estándar.")
print(f"Ver 10 horas de un curso estándar equivalen a {dalto_entre_media*10} horas del curso de Dalto.")

print("----------------------------------------------------------------")