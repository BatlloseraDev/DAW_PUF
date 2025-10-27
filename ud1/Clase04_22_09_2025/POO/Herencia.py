class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido")

    def mover(self):
        print("El vehículo se está moviendo")


class Coche(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super(Coche, self).__init__(marca, modelo)
        self.puertas = puertas

    def mover(self):  # Sobrescribimos el método
        print(f"El coche {self.marca} {self.modelo} circula por la carretera con {self.puertas} puertas")

    def tocar_claxon(self):
        print("¡piiiip piiip!")


# ------------------------------
# Uso
# ------------------------------
print(Vehiculo.__subclasses__())
print(Coche.__bases__)
v1 = Vehiculo("Genérico", "X")
c1 = Coche("Toyota", "Corolla", 4)

v1.mover()
c1.mover()
c1.tocar_claxon()



