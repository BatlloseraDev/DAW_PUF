from urllib.parse import uses_query

from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Usuario.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA USUARIOS'))
            Usuario.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Usuarios ya esta vacia'))

        if Direccion.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA DIRECCIONS'))
            Direccion.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Direcciones ya esta vacia'))

        if Autor.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA AUTOR'))
            Autor.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Autores ya esta vacia'))
        if Cancion.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA CANCION'))
            Cancion.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Canciones ya esta vacia'))

        if Podcast.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA PODCAST'))
            Podcast.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Podcast ya esta vacia'))

        if Reproducciones.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'VOY A BORRAR DATOS DE LA TABLA REPRODUCCION'))
            Reproducciones.objects.all().delete()
        else:
            self.stdout.write(self.style.WARNING(f'Reproducciones ya esta vacia'))
