class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos {self.apellidos}"

    def identificacion(self):
        return f"{self.nombre} , {self.apellidos}"
    def identificacion1(self):
        return f"{self.nombre} , {self.apellidos}"


class Alumno(Persona):
    def __init__(self, nombre, apellidos, curso):
        super().__init__(nombre, apellidos)
        self.curso = curso

    def __str__(self):
        return f"{super().__str__()} y curso: {self.curso}"

    def identificacion1(self):
        return f"{self.nombre} , {self.apellidos}, {self.curso}"
    

alumno= Alumno("Alumno", "ap1,ap2", "daw")
print(alumno.identificacion1())