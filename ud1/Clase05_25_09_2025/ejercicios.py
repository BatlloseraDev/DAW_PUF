
class Alumno:
    def __init__(self, nombre, edad, clase):
        self.nombre = nombre
        self.edad = edad
        self.clase = clase

    def __str__(self):
        return f"Alumno({self.nombre}, {self.edad}, {self.clase})"



alumnos = [
    Alumno("Francisco", 20, "DAW"),
    Alumno("Ana", 21, "DAM"),
    Alumno("Luis", 19, "DAW"),
]

'''
Actividad 1.Realizar un metodo de busqueda para buscar en la lista de alumnos, por el nombre de alguno de los elementos que se encuentra en la lista
Actividad 2. Mediante el uso de getattr realizar un metodo general para buscar sobre cualquier atributo de una lista de objetos pasandole como parametro
el nombre del atributo y el valor a buscar.
Actividad 3. Aula, entregable.

'''

# ejercicio 1


def busquedaEnLista(lista, nombre):

    for elemento in lista:
        if elemento.nombre == nombre:
            return True
    return False

nombre = input("Introduce el nombre del alumno")
if busquedaEnLista(alumnos, nombre):
    print("el alumno se encuentra en la lista")
else:
    print("el alumno no se encuentra en la lista")

#ejercicio 2

def busquedaConGetAttr(listaObjetos,nombreParametro, valorParametro):

    for elemento in listaObjetos:
        try:
            if getattr(elemento, nombreParametro) == valorParametro:
                return True
        except Exception as e:
            print(f'fallo en el nombre del elemento: {nombreParametro}: {e}')
            break

    return False

nombre=input("Introduce el nombre del atributo del alumno")
valor = input("Introduce el valor del parametro del alumno")


if busquedaConGetAttr(alumnos,nombre,valor ):
    print (f'el parametro con el parametro {nombre} y valor {valor}se encuentra en la lista')


#ejercicio 3