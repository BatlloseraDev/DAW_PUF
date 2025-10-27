from django.core.management.base import BaseCommand
from datetime import date, timedelta

from ...models import *


class Command(BaseCommand):
    help = 'Comando Inicial'
    def handle(self, *args, **options):
        programador = Programador(nombre='Programador Recien Nacido', apellido='joven')
        programador.fecha_nacimiento = date.today() - timedelta()
        programador.save()


