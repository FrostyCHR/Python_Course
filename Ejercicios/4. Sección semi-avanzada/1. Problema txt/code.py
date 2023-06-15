nombres = ["Lucas", "Fernando", "Alejandra", "Damián", "Mariana"]
apellidos = ["Dalto", "Hierro", "Torrejón", "Pérez", "Garzón"]

# Se podría hacer el for en una sola línea, pero no se me ocurrió y solo haría el código más lioso.
with open("Ejercicios\\4. Sección semi-avanzada\\1. Problema txt\\txt_file.txt", "w", encoding="UTF-8") as archivo:
    for index,datos in enumerate(zip(nombres,apellidos)):
        archivo.write(f"Persona {index+1}: {datos[0]} {datos[1]}.\n")
    archivo.write("\nIs this a Persona refenence?")