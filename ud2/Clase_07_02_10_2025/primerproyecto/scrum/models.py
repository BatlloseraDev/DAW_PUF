from django.db import models
from django.utils import timezone

# Create your models here.
class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    ROLES = [
        ('PR', 'Programador'),
        ('TE', 'Tester'),
        ('JP', 'Jefe de proyecto'),
    ]
    rol = models.CharField(max_length=2, choices=ROLES, default='PR')
    TECNOLOGIA = [('P','PYTHON'),
                  ('J','JAVA'),
                  ('PHP','PHP')]
    tecnologia = models.CharField(max_length=3, choices=TECNOLOGIA, default='P')

    def __str__(self):
        return f"Programador: {self.id} nombre {self.nombre}  apellido: {self.apellido}, fecha de nacimiento {self.fecha_nacimiento}, rol {self.rol}"


class Sprint(models.Model):
    nombreSprint = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Sprint: {self.nombreSprint} {self.fecha_inicio} {self.fecha_fin}"



class Tarea(models.Model):
    nombreTarea= models.CharField(max_length=50)
    descripcion= models.TextField(max_length=100)
    estimacion = models.IntegerField(null=True,blank=True)
    asignada = models.BooleanField(default=False)
    #usuario = models.ForeignKey(Programador, on_delete=models.CASCADE, related_name="programador", null=True, blank=True)
    usuario = models.ManyToManyField(Programador)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name="sprint", null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.nombreTarea} {self.descripcion} {self.estimacion} {self.asignada} {self.usuario}"

