from datetime import datetime
import os

#f = open("Libro2.txt","r")
#Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values (seq_personas.nextval("personas_seq", "Francisco", "Alia", "04/05/1992","Falsa","123","+34666666666");

rutaLectura = "Libro2.txt"
rutaEscritura = "logs"

informacionParseada =[]

with open(rutaLectura,"r") as f:
    linea = f.read().splitlines()
    for datos in linea:
        contenido = datos.split("\t")
        datos_limpios = [elemento for elemento in contenido if elemento != '']
        informacionParseada.append(datos_limpios)



for datos in informacionParseada:
    fecha = datetime.now().strftime("%d%m%Y")
    nombre_fichero = f"{rutaEscritura}/{fecha}_Persona.log"
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero,"a") as f:
            formateado = f"Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values (seq_personas.nextval(personas_seq, {datos[0]}, {datos[1]}, {datos[2]},{datos[3]},{datos[4]},{datos[5]});\n"
            f.write(formateado)
    else:
        with open(nombre_fichero,"w") as f:
            formateado = f"Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values (seq_personas.nextval(personas_seq, {datos[0]}, {datos[1]}, {datos[2]},{datos[3]},{datos[4]},{datos[5]});\n"
            f.write(formateado)


# fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#nombre_fichero = f"logs/{fecha}{nombre}_Persona.log"

#print(fecha)

#with open("nuevo_fichero.txt", "a") as f:
 #   f.write(fecha)

#rutaEscritura = "log"
#la variable rutaEscritura no la usas luego en la línea 23 o haces a mano. Cuidado creo que nos podriamos ahorrar desde la lina 28 pero esta bien.



