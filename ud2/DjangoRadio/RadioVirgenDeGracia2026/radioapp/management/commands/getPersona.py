from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):

    def handle(self, *args, **options):

        persona = Usuario.objects.get(pk=202)

        direcciones = PersonaDireccion.objects.filter(usuario=persona)
        numeroCallePreferida= int(input("Inserta el numero de calle preferida:\n"))

        for direccion in direcciones:
            if direccion.direccion.numero == numeroCallePreferida:
                direccion.preferida = True
            else:
                direccion.preferida = False
            direccion.save()