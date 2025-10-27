'''
Abrir un fichero
La función open() se utiliza para abrir un fichero en Python. Tiene dos parámetros importantes:
    El nombre del fichero que quieres abrir.
    El modo en que quieres abrir el fichero (lectura, escritura, etc.).
    f = open("nombre_fichero.txt", "modo")

    Los modos más comunes son:
        "r": Leer. El fichero debe existir.
        "w": Escribir. Si el fichero no existe, se crea; si existe, se sobrescribe.
        "a": Añadir. Escribe al final del fichero sin sobrescribir el contenido existente.
        "r+": Leer y escribir.
'''
f = open("archivo.txt", "r")
print(f.read())
#Después de trabajar con un fichero, es importante cerrarlo para liberar recursos. Usamos el métdo close() para ello:
f.close()

'''
readline()
Lee una línea del fichero a la vez.
'''
with open("variasLineas.txt", "r") as f:
    linea = f.readline()
    while linea:
        print(linea, end="")
        linea = f.readline()


with open("variasLineas.txt", "r") as f:
    print('LEER TODO')
    lineas = f.readlines()
    print(lineas, end="")
