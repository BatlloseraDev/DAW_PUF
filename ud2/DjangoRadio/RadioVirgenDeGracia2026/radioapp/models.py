from django.db import models
from datetime import date
from faker import Faker
import random

# Create your models here.
class Direccion(models.Model):
    CIUDADES = [('CR','CIUDAD REAL'), ('ARG','ARGAMASILLA'), ('PUER','PUERTOLLANO'), ('AML','ALMODOVAR')]
    calle = models.CharField(max_length=10)
    numero = models.IntegerField(null=True,blank=True)
    ciudad = models.CharField(choices=CIUDADES)
    def __str__(self):
        return f"{self.calle} {self.id}"

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'



class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nick = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        print('Voy a guardar una persona')
        persona = super().save(*args, **kwargs)
        #hago lo que me da la gana
        print('ya la he guardado')
        #Cancion.objects.create(nombre="Sangre",duracion="180",ano_lanzamiento="1992")
        '''if self.pk is not None:
            fake = Faker('es_Es')
            codigo_random = random.choice([codigo for codigo, _ in Direccion.CIUDADES])
            direccion = Direccion.objects.create(calle=fake.address(), numero=fake.port_number(),
                                                 ciudad=codigo_random)
            direccion.save()

            personaDirecciones = PersonaDireccion.objects.filter(usuario=persona)
            for personaDireccion in personaDirecciones:
                personaDireccion.preferida = False
                personaDireccion.save()

            nuevaPersonaDireccion = PersonaDireccion.objects.create(direccion=direccion, usuario=persona, preferida=True)
            nuevaPersonaDireccion.save()
            print(" guardado la cancion")
        '''
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def __str__(self):
        return f"{self.id} {self.nombre} {self.nick}"

    class Meta:
        ordering = ['nombre','apellido']
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

class PersonaDireccion(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    preferida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.usuario.nombre} {self.direccion.calle}"

    class Meta:
        unique_together = ['direccion', 'usuario']
        verbose_name = 'Persona Dirección'
        verbose_name_plural = 'Persona Direcciones'



class Autor(models.Model):
    GENEROS = [('Pop', 'Pop'), ('Rap', 'Rap'), ('Reggeton', 'Reggeton'), ('Electronica', 'Electronica')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    genero = models.CharField(choices=GENEROS,max_length=12)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.genero}"
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Cancion(models.Model):
    nombre = models.CharField(max_length=20)
    ano_lanzamiento = models.IntegerField()
    duracion = models.IntegerField()
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,null=True,blank=True )

    def __str__(self):
        return f"{self.id} {self.nombre} duracion:{self.duracion} autor:{self.autor}, año lanzamiento:{self.ano_lanzamiento} "
    class Meta:
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'


class Podcast(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    TEMATICAS= [('Actualidad','Actualidad'), ('Investigacion','Investigacion'),('Terror','Terror')]
    tematica = models.CharField(choices=TEMATICAS,max_length=20,blank=True,null=True)
    autores = models.ManyToManyField(Autor)
    def __str__(self):
        return f"{self.id} {self.nombre} descripcion {self.descripcion} tematica:{self.tematica}"
    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'

class Reproducciones(models.Model):
    cancion = models.ForeignKey(Cancion,on_delete=models.CASCADE, blank=True,null=True)
    podcast = models.ForeignKey(Podcast,on_delete=models.CASCADE, blank=True,null=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.cancion} {self.podcast} {self.usuario}"
    class Meta:
        verbose_name = 'Reproducción'
        verbose_name_plural = 'Reproducciones'