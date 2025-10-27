from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            direccion = Direccion.objects.all()[0]

            persona = Usuario.objects.get(pk=264)

            personaDireccion = PersonaDireccion.objects.create(
                direccion=direccion,
                usuario=persona,
                preferida=False
            )
            personaDireccion.save()




            #personas = Usuario.objects.filter(fecha_nacimiento__range=["1985-01-01","2007-12-31"],nombre__icontains="na")
            #print(f'personas: {personas[0]}')
            #for persona in personas:
            #    direccion = Direccion(calle='Falsa', numero='123', ciudad='CR')
            #    direccion.save()
            #    persona.direccion = direccion
            #    persona.save()
            #    print("Se ha actualizado la persona correctamente")
            #personas = Usuario.objects.all()
        except Exception as e:
            print(f'se ha producido un fallo {e}')