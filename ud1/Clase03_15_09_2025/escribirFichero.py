'''
write()
Escribe una cadena en el fichero. Si el fichero no existe, se crea. Si ya existe, se sobrescribe (si usas el modo "w").
'''
with open("nuevo_fichero.txt", "w") as f:
    f.write("Buenos días, a por el jueves.\n")

'''
writelines()
Escribe una lista de cadenas en el fichero.
'''
lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]

with open("nuevo_fichero.txt", "w") as f:
    f.writelines(lineas)

'''
Añadir a un fichero ("a")
Si deseas añadir contenido a un fichero sin sobrescribir el existente, usa el modo "a".
'''
with open("nuevo_fichero.txt", "a") as f:
    f.write("Añadiendo esta nueva línea al final.\n")

'''
Leer y escribir ("r+")
El modo "r+" permite leer y escribir en un fichero sin sobrescribir su contenido inicial.
'''
with open("nuevo_fichero.txt", "r+") as f:
    contenido = f.read()
    print(contenido)
    f.write("\nAñadiendo una línea desde el modo r+.")
