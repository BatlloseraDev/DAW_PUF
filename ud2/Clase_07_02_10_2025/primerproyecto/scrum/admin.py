from django.contrib import admin
from .models import Programador
from .models import Tarea
from .models import *
# Register your models here.
admin.site.register(Programador)
admin.site.register(Tarea)
admin.site.register(Sprint)