from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from datetime import date
from dateutil.relativedelta import relativedelta
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    help = 'este busca el usuario con la edad entre 20 y 40 años y que tengan la palabra na'

    def handle(self, *args, **options):
        fake = Faker('es_Es')
        try:
            hoy = date.today()
            fecha_limite_minima = hoy - relativedelta(years=40)
            fecha_limite_maxima = hoy - relativedelta(years=20)
            personas = Usuario.objects.filter(fecha_nacimiento__range=[fecha_limite_minima,fecha_limite_maxima],nombre__icontains="an")
            if personas:
                persona = personas[0]
                codigo_random = random.choice([codigo for codigo, _ in Direccion.CIUDADES])
                direccion = Direccion.objects.create(calle=fake.address(), numero=fake.port_number(),
                                                     ciudad=codigo_random)
                direccion.save()

                personaDirecciones= PersonaDireccion.objects.filter(usuario = persona)
                for personaDireccion in personaDirecciones:
                    personaDireccion.preferida= False
                    personaDireccion.save()

                nuevaPersonaDireccion = PersonaDireccion.objects.create(direccion=direccion, usuario=persona, preferida=True)
                nuevaPersonaDireccion.save()
                print(f'persona actualizada correctamente {persona}')
            else:
                print('no se encontraron personas')


        except Exception as e:
            print(f'se ha producido un fallo {e}')
