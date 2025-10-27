from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random

class Command(BaseCommand):
    help = 'este busca el usuario que haya nacido entre x fecha y otra y muestra sus reproducciones'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id',
            type=int,
            required=True,
            help='id de una cancion')
        parser.add_argument(
            '--prefer',
            type=bool,
            required=False,
            help='Indica si tengo que hacer algo'
        )


    def handle(self, *args, **options):

        id= options.get('id')
        prefer = options.get('prefer')
        if prefer:
            print('Lo cojo')
        else:
            print('No lo cojo')
        cancion = Cancion.objects.get(pk=id)
        print(cancion)