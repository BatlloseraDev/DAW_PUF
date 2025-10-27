from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    help = 'este busca el usuario que haya nacido entre x fecha y otra y muestra sus reproducciones'

    def handle(self, *args, **options):
        try:
            personas = Usuario.objects.filter(fecha_nacimiento__range=["1992-01-01", "2006-12-31"])
            if personas:
                for persona in personas:
                    reproducciones = Reproducciones.objects.filter(usuario=persona)
                    if reproducciones:
                        for reproduccion in reproducciones:
                            if reproduccion.podcast is None:
                                self.stdout.write(self.style.SUCCESS(f'La persona: {persona.nombre} reprodujo la canción:{reproduccion.cancion.nombre}'))
                            else:
                                self.stdout.write(self.style.SUCCESS(f'La persona: {persona.nombre} reprodujo el podcast:{reproduccion.podcast.nombre}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'La persona{persona.nombre} no reprodujo nada'))
                    print('---------------------------------------------------')
            else:
                self.stdout.write(self.style.SUCCESS('No hay personas en esas fechas'))

        except Exception as e:
            print(f'se ha producido un fallo {e}')