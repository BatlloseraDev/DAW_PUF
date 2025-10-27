class Persona:
    contador = 0
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        Persona.contador += 1
        if identificador is None:
            self.__identificador = Persona.contador
        else:
            self.__identificador = identificador
        self._puntuacion_total = 0

    def __str__(self):
        return f"[Nombre y Apellidos] {self.__nombre} {self.__apellidos} [Fecha Nac] {self.__fecha_nacimiento}"


    @property #solo get ya que set va a ser calculado por la propia clase al momento de crearse.
    def puntuacion_total(self):
        return self._puntuacion_total

    #getters and setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, value):
        self.__identificador = value

