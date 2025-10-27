from django.core.management.base import BaseCommand

from ...models import *



class Command(BaseCommand):
    help = 'Modifica los datos de sergio'
    def handle(self, *args, **options):
        programadores = Programador.objects.filter(nombre="Sergio")
        for prog in programadores:
            prog.nombre = "Tchoameni"
            prog.save()

