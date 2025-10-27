class Edificio:

    __variableRara= 20


    def __init__(self, puertas, plantas, ventanas= None):
        self.__puertas = puertas
        self.__ventanas = ventanas
        self.__plantas = None


    def __str__(self):
        return f"{self.__puertas} puertas y  {self.__ventanas} ventanas"

    def set_ventanas(self, ventanas):
        if ventanas <0:
            raise ValueError("Ventanas no puede ser negativa.")
        self.__ventanas = ventanas
    def get_ventanas(self):
        return self.__ventanas

    @staticmethod
    def get_variableRara():
        return variableRara



print(Edificio.variableRara)

edificio = Edificio(10,20,30)
edificio2 = Edificio(10,30)
print(edificio2)

try:
    edificio.set_ventanas(20)
    print(f"el edificio tiene {edificio.get_ventanas()}")
    edificio.set_ventanas(-30)
    print(f"el edificio tiene {edificio.get_ventanas()}")


except Exception as e:
    print(f"has tenido un error cambiando las ventanas: {e}")