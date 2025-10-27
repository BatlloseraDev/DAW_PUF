from urllib.parse import uses_query

from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('INICIAMOS LA CARGA DE LOS DATOS'))
        #user= Usuario(nombre='Francisco')
        #user.save()
        #Usuario.objects.create(nombre='Francisco')
        fake = Faker('es_Es')
        modelos= [Direccion, Usuario, Autor, Cancion, Podcast]#bucle
        codigos = [codigo for codigo, _ in Direccion.CIUDADES]
        generos = [genero for genero,_ in Autor.GENEROS]
        tematicas = [tematica for tematica, _ in Podcast.TEMATICAS]

        if Usuario.objects.exists() or Cancion.objects.exists() or Podcast.objects.exists() or Reproducciones.objects.exists() or Autor.objects.exists() or Direccion.objects.exists() :
            self.stdout.write(self.style.WARNING(f'Tiene ya datos'))
        else:


            #usuarios
            for i in range(20):
                Usuario.objects.create(nombre=fake.first_name(), apellido=fake.last_name(), nick=fake.user_name(),fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=18),telefono=fake.phone_number(), email=fake.email())
                self.stdout.write(self.style.SUCCESS(f'La persona {i} creada exitosamente'))
            #direccionUsuario
            usuarios = Usuario.objects.all()

            for usuario in usuarios:
                for i in range(2):

                    codigo_random = random.choice(codigos)
                    direccion = Direccion.objects.create(calle=fake.address(), numero=fake.port_number(), ciudad=codigo_random)
                    direccion.save()

                    PersonaDireccion.objects.create(direccion=direccion, usuario=usuario,preferida= (i==0))
            #Autores
            for i in range(20):
                genero = random.choice(generos)
                autor = Autor.objects.create(nombre=fake.first_name(), apellido=fake.last_name(), genero=genero)
                autor.save()
                self.stdout.write(self.style.SUCCESS(f'El autor {i} creado exitosamente'))

            #cancion
            for i in range(30):
                #coger un autor random
                autores = Autor.objects.all()
                autor=random.choice(autores)
                cancion = Cancion.objects.create(nombre=f"La {fake.word()} de {fake.word()}", ano_lanzamiento=int(fake.year()),duracion=fake.numerify(),autor = autor)
                cancion.save()
                self.stdout.write(self.style.SUCCESS(f'La cancion {i} creada exitosamente'))

            #podcast
            for i in range(50):
                tematica = random.choice(tematicas)
                podcast = Podcast.objects.create(
                    nombre=fake.catch_phrase()[:20],
                    descripcion=fake.text(),
                    tematica=tematica,
                )
                autores = Autor.objects.all()
                num_autores = random.randint(1, 3)
                autores_podcast = random.sample(list(autores), num_autores)
                podcast.autores.add(*autores_podcast)
                podcast.save()
                self.stdout.write(self.style.SUCCESS(f'El podcast {i} creado exitosamente'))
            #reproducciones

            for i in range(500):
                eleccion= random.choice([True, False])
                usuario = random.choice(Usuario.objects.all())

                reproduccion= None
                if eleccion:
                    elemento=random.choice(Cancion.objects.all())
                    reproduccion=Reproducciones.objects.create(cancion= elemento,usuario=usuario)
                else:
                    elemento=random.choice(Podcast.objects.all())
                    reproduccion=Reproducciones.objects.create(podcast=elemento ,usuario=usuario)
                reproduccion.save()
                self.stdout.write(self.style.SUCCESS(f'La reproduccion {i} creada exitosamente'))
