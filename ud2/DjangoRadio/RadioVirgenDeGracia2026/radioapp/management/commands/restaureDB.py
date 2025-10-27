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

