
import random as r
from modelos.persona import Persona

class Villano(Persona):


    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador ,**kwargs):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.__chagepeteador= kwargs.get("chagepeteador",generarValorAleatorio())
        self.__entregadorTardio= kwargs.get("entregadorTardio",generarValorAleatorio())
        self.__ausencias = kwargs.get("ausencias",generarValorAleatorio())
        self.__hablador = kwargs.get("hablador",generarValorAleatorio())
        self.__calcular_puntuacion()


    def __str__(self):
        base = super().__str__()
        return f"Villano: {base} [Chatgepeteador]{self.__chagepeteador}, [Entregador Tardio]{self.__entregadorTardio}, [Ausencias]{self.__ausencias}, [Hablador]{self.__hablador}. [Puntuacion total] {self._puntuacion_total}"


    def __calcular_puntuacion(self):
        contador = round(
            self.__chagepeteador * 0.5 + self.__entregadorTardio * 0.3 + self.__ausencias * 0.1 + self.__hablador * 0.1) #ecuacion de importacia de atributos
        self._puntuacion_total = contador



    #getters and setters
    @property
    def chagepeteador(self):
        return self.__chagepeteador

    @property
    def entregadorTardio(self):
        return self.__entregadorTardio

    @property
    def ausencias(self):
        return self.__ausencias

    @property
    def hablador(self):
        return self.__hablador







def generarValorAleatorio():
    return r.randint(1, 100)