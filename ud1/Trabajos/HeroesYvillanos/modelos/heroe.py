import random as r

from modelos.persona import Persona

class Heroe(Persona):



    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador, **kwargs):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.__codigoLimpio = kwargs.get("codigoLimpio",generarValorAleatorio())
        self.__bienDocumentado= kwargs.get("bienDocumentado",generarValorAleatorio())
        self.__gitgod= kwargs.get("gitgod",generarValorAleatorio())
        self.__arquitecto= kwargs.get("arquitecto",generarValorAleatorio())
        self.__detallista = kwargs.get("detallista",generarValorAleatorio())
        self.__calcular_puntuacion()

    def __calcular_puntuacion(self):
        operacion = round(
            self.__codigoLimpio * 0.4 + self.__bienDocumentado * 0.1 + self.__gitgod * 0.2 + self.__arquitecto * 0.2 + self.__detallista * 0.1) #ecuacion de importacia de atributos
        self._puntuacion_total = operacion


    def __str__(self):
        base = super().__str__()
        return f"Heroe: {base} [Codigo Limpio]{self.__codigoLimpio}, [Bien Documentado]{self.__bienDocumentado}, [Git God]{self.__gitgod}, [Arquitecto]{self.__arquitecto}, [Detallista]{self.__detallista}. [Puntuacion total] {self._puntuacion_total}"


    #getter and setter
    #estos parametros solo van a ser de get ya que lo calculo en la clase
    @property
    def codigoLimpio(self):
        return self.__codigoLimpio


    @property
    def bienDocumentado(self):
        return self.__bienDocumentado
    @property
    def gitgod(self):
        return self.__gitgod
    @property
    def arquitecto(self):
        return self.__arquitecto
    @property
    def detallista(self):
        return self.__detallista




def generarValorAleatorio():
    return r.randint(1, 100)