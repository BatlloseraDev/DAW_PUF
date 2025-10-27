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
        usuario = Usuario(nombre ="Francisco",apellido = "Alia",nick="alion1",telefono="222",fecha_nacimiento=date.today())
        usuario.save()