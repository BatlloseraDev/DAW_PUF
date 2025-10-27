class Ordenador:
    def __init__(self, grafica, cpu, refrigeracion):
        self.__grafica = grafica
        self.__cpu = cpu
        self.__refrigeracion = refrigeracion

    @property
    def grafica(self):
        return self.__grafica

    @grafica.setter
    def grafica(self, grafica):
        self.__grafica = grafica

    @property
    def cpu(self):
        return self.cpu

    @cpu.setter
    def cpu(self, value):
        self.cpu = value

    @property
    def refrigeracion(self):
        return self.refrigeracion

    @refrigeracion.setter
    def refrigeracion(self, value):
        self.refrigeracion = value


ordenador = Ordenador(grafica="RTX 4090", cpu="x", refrigeracion="y")



print(ordenador.grafica)
print(ordenador.__dict__)