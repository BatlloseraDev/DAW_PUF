#una tarea nueva y dos programadores que ya esten en la base de datos
from django.core.management.base import BaseCommand

from ...models import *

class Command(BaseCommand):
    help = 'Crear Tarea'
    def handle(self, *args, **options):
        programadores = Programador.objects.filter(nombre="Tchoameni")
        progs = (programadores[0],programadores[1])
        sprint = Sprint.objects.get(id=1)
        tarea = Tarea(nombreTarea="Probamos en clase",descripcion="ejercicios",estimacion=10,asignada=1, sprint=sprint)
        tarea.save()
        tarea.usuario.set(progs)


