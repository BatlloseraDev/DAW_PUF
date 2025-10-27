import random

from modelos.heroe import Heroe
from modelos.villano import Villano
from datetime import  date

from utilidades.fileManager import FileManager
from utilidades.helpers import Helper
from utilidades.logger import Logger




def controladorTeclado(texto, tipoDato): #Para controlar los datos que pido por teclado
    texto = texto.strip() #controlo los espacios
    if tipoDato == "entero":
        try:
            dato= int(texto)
            return dato
        except ValueError:
            return None

    elif tipoDato == "texto":
        if texto == "":
            return None
        else:
            return texto.replace('/',' ') #el replace se encarga de arreglar el hecho de que el usuario haya introducido un caracter no deseado
    else:
        return None



def menu():#Menu creado por el profesor
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para enfrentar un heroe contra un villano")
    print("5) Para salir")


def gestionAulaDeHeroesYVillanos(opcion):#reutilizado el metodo para gestionar la creacion de personajes
    valores = {
        'nombre': controladorTeclado(input("Ingrese el nombre: "), "texto"),
        'apellidos': controladorTeclado(input("Ingrese los apellidos: "), "texto")}

    dia_nacimiento = controladorTeclado(input("Ingrese el dia nacimiento: "), "entero")
    mes_nacimiento = controladorTeclado(input("Ingrese el mes nacimiento: "), "entero")
    anio_nacimiento = controladorTeclado(input("Ingrese el anio nacimiento: "), "entero")

    if None in [dia_nacimiento, mes_nacimiento, anio_nacimiento]:
        return False, f"Algun campo de la fecha no fue valido, será representado con None: d{dia_nacimiento}, m{mes_nacimiento}, y{anio_nacimiento}"
    else:
        try:
            fecha_nacimiento = date(anio_nacimiento, mes_nacimiento, dia_nacimiento)
            valores['fecha_nacimiento'] = fecha_nacimiento
        except Exception as e:
            return False, f"la fecha no es valida: {e}"

    if None in valores.values():
        return False, f"algún campo no fue introducido correctamente en nombres{valores["nombre"]} o apellidos{valores["apellidos"]} "

    if opcion == 1:
        heroe = Heroe(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"],None)
        return True,"héroe creado" ,heroe
    elif opcion == 2:
        # guardar en data
        return True,"villano creado" ,Villano(valores["nombre"], valores["apellidos"], valores["fecha_nacimiento"], None)
    else:
        return False, "el desarrollador introdujo una opción no valida para probar"




def cargar_personas(ruta,tipo,listaPersonas,log): #metodo para el volcado de información de los personajes creados
    info= FileManager.lector(ruta)
    if info[0]:
        log.log("INFO", f"Información de los {tipo} recuperada de la base de datos exitosamente: {info[1]}")
        for persona in info[2]:
            listaPersonas.append(persona)
    else:
        log.log("ERROR", f"fallo en la lectura de los {tipo} en la base de datos:{info[1]}")




def buscar_personajes(listaPersonas,log): #codigo utilizado para buscar por atributos de los personajes existentes

    try:#protege el sistema de algun dato erroneoy lo almacena en el log
        print("Que quieres buscar:\n1)Heroes\n2)Villanos")
        opcionBusqueda = int(input())
        arrayClaveValor=[""]
        if opcionBusqueda == 1:
            arrayClaveValor= ["nombre","apellidos","fecha_nacimiento","identificador","codigoLimpio","bienDocumentado","gitgod","arquitecto","detallista","puntuacion_total"]
            print("Por cual atributo quieres buscar:\n1)nombre\n2)apellidos\n"
                  "3)fecha nacimiento\n4)id\n5)codigo limpio\n"
                  "6)bien documentado\n7)git god\n8)arquitecto\n"
                  "9)detallista\n10)puntuación")
            print(arrayClaveValor)
        elif opcionBusqueda == 2:
            arrayClaveValor = ["nombre", "apellidos", "fecha_nacimiento", "identificador", "chagepeteador",
                               "entregadorTardio", "ausencias", "hablador", "puntuacion_total"]
            print("Por cual atributo quieres buscar:\n1)nombre\n2)apellidos\n"
                  "3)fecha nacimiento\n4)id\n5)chatgepeteador\n"
                  "6)entregador tardio\n7)ausencias\n8)hablador\n"
                  "9)puntuación")

        else:
            log.log("ERROR","El usuario intentó buscar una opción no valida entre heroes y villanos")
            return


        tipoDato = int(input()) - 1
        valor = input(f"Ingrese el valor del tipo del dato: {arrayClaveValor[tipoDato]} \n") #aqui podría reutilizar lo de ingresar tipo dato
        encontrado = False
        for personaje in listaPersonas:
            if opcionBusqueda == 1 and isinstance(personaje,Villano): #de esta manera evito la busqueda de personaje
                pass
            elif opcionBusqueda == 2 and isinstance(personaje,Heroe):
                pass
            else:
                if f"{getattr(personaje, arrayClaveValor[tipoDato])}" == valor:#al ser de dos tipos distintios me da error en la búsqueda lo soluciono cambiando el valor a string
                    print(f"Personaje encontrado: {personaje}")
                    encontrado = True
                    log.log("INFO", f"se encontró una coincidencia: {personaje}")
        if not encontrado:
            log.log("INFO",f"no se encontró ninguna coincidencia con el valor: {valor}")
            print(f"no se encontró ninguna coincidencia con el valor: {valor}")

    except Exception as e:
        log.log("ERROR",f"El usuario introdujo un dato erroneo: {e}")



def iniciar_enfrentamiento(listaPersonas,log):


    if not any(isinstance(p, Villano) for p in listaPersonas) or not any(isinstance(p, Heroe) for p in listaPersonas):#comrpueba de que al menos alla uno de ambos, si no lo cumple se sale
        print("No se puede realizar el enfrenamiento ya que no existe al menos un héroe y un villano")
        log.log("ERROR", "Para realizar el enfrentamiento al menos debe existir un héroe y un villano")
        return

    cantidadPersonas = len(listaPersonas)
    intentos = 0
    heroeEncontrado = False
    villanoEncontrado = False
    enfrentamieto = []
    numeroRandom = random.randint(1,cantidadPersonas)-1
    while cantidadPersonas > intentos and (not villanoEncontrado or not heroeEncontrado): #un bucle sencillo para buscar ambos
        if isinstance(listaPersonas[numeroRandom], Villano) and not villanoEncontrado:
            villanoEncontrado = True
            enfrentamieto.append(listaPersonas[numeroRandom])
        elif isinstance(listaPersonas[numeroRandom], Heroe) and not heroeEncontrado:
            heroeEncontrado = True
            enfrentamieto.append(listaPersonas[numeroRandom])
        intentos += 1
        numeroRandom +=1
        if numeroRandom == cantidadPersonas: #si llega al maximo que empiece desde el principio mientras que queden intentos
            numeroRandom= 0

    log.log("INFO", f"enfrentamiento encontrado entre: {enfrentamieto[0]} y {enfrentamieto[1]}")
    print(f"Enfrentamiento encontrado, se va a enfrentar {enfrentamieto[0].nombre} {enfrentamieto[0].apellidos} vs {enfrentamieto[1].nombre} {enfrentamieto[1].apellidos}")
    resultado= abs(enfrentamieto[0].puntuacion_total - enfrentamieto[1].puntuacion_total)
    if resultado <=10:
        log.log("INFO",f"El resultado entre los dos fue empate: personaje 1: {enfrentamieto[0].puntuacion_total} y  personaje 2: {enfrentamieto[1].puntuacion_total}")
        print("El resultado entre los dos fue empate, sus fuerzas estaban muy parejas")
    else:
        if enfrentamieto[0].puntuacion_total>enfrentamieto[1].puntuacion_total:
            log.log("INFO",f"Ganó el personaje: {enfrentamieto[0].nombre}")
            print(f"Ganó el personaje: {enfrentamieto[0].nombre} {enfrentamieto[0].apellidos}con una fuerza de {enfrentamieto[0].puntuacion_total}")
        else:
            log.log("INFO", f"Ganó el personaje: {enfrentamieto[1].nombre}")
            print(f"Ganó el personaje: {enfrentamieto[1].nombre} {enfrentamieto[1].apellidos} con una fuerza de {enfrentamieto[1].puntuacion_total}")



def main(): #main donde se desarrolla el programa
    log = Logger()
    log.log("INFO","Inici1ado el sistema")

    #volcado inicial de datos
    listaPersonas = []

    try:
        cargar_personas(Helper.rutaGuardadoHeroe,"Héroes",listaPersonas,log)
        cargar_personas(Helper.rutaGuardadoVillano,"Villanos",listaPersonas,log)


        while True:
            menu()
            opcion = int(input("Que eliges\n"))

            if opcion == 3:
                log.log("INFO","Iniciado el proceso de busqueda de personaje")
                buscar_personajes(listaPersonas,log)
            elif opcion == 4:

                iniciar_enfrentamiento(listaPersonas,log)

            elif opcion == 5:
                log.log("INFO","El usuario finalizó la sesión")
                break
            elif opcion >= 6 or opcion <= 0:
                print("Opción invalida")
                log.log("ALERT",f"El usuario falló y no introdujo correctamete la opción: {opcion}")
            else:
                log.log("INFO","Iniciado el proceso de creación de Héroe o Villano")
                resultado = gestionAulaDeHeroesYVillanos(opcion)
                if resultado[0]:
                    listaPersonas.append(resultado[2])
                    log.log("INFO",resultado[2])
                    guardado= Helper.convertirObjetoATexto(resultado[2])
                    if guardado[0]:
                        FileManager.guardar(Helper.devolverRutaGuardado(opcion),guardado[1]) #los guardo por separado por diseño mio, se podrían guardar en el mismo fichero sin problemas
                        log.log("INFO","El personaje fue guardado correctamente en la base de datos")
                    else:
                        log.log("Error",f"error al guardar en la base de datos: {guardado[1]}")

                else:
                    print(f"Error en la creación de personaje, volviendo al menú: {resultado[1]}")
                    log.log("ERROR",f"Hubo un error creando el personaje: {resultado[1]}")


    except Exception as e:
        log.log("ERROR", f"{e}") # {traceback.format_exc()} para devolver la ultima linea del error
        log.log("INFO","Cerrando el sistema automaticamente")
    except KeyboardInterrupt:
        log.log("INFO", "El usuario cerró el programa abruptamente")#Busqué como controlar el error que aparece cuando se cierra el programa desde fuera


if __name__ == "__main__":
    main()





