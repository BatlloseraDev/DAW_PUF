import json

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *



# Create your views here.
def get_cancion(request,id):
    #if request.user.is_authenticated:
    if request.method == 'GET':
        try:
            cancion = Cancion.objects.all().values('id' , 'nombre').filter(id=id)
            return JsonResponse(list(cancion), safe=False)
        except Cancion.DoesNotExist:
            return JsonResponse({'error':"Canción no encontrada"}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def add_cancion(request):
    if request.method == 'POST':
        try:
            jsonCancion = json.loads(request.body)
            Cancion.objects.create(**jsonCancion)
            return JsonResponse({"mensaje": "se ha insertado correctamente"}, safe=False)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error':"Error de json desconocido"}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def get_canciones(request):

    if request.method == 'GET':
        try:
            canciones= Cancion.objects.all()
            return JsonResponse(list(canciones.values()), safe=False)
        except Cancion.DoesNotExist:
            return JsonResponse({'error':"No existen canciones"}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_cancion(request,id):
    if request.method == 'DELETE':
        try:
            cancion = Cancion.objects.get(id=id)
            cancion.delete()
            return JsonResponse({"mensaje": "se ha eliminado"}, safe=False)
        except Cancion.DoesNotExist:
            return JsonResponse({'error':"No existen canciones"}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_cancion(request,id):
    if request.method == 'PUT':
        try:
            jsonCancion = json.loads(request.body)
            cancion = Cancion.objects.get(id=id)
            cancion.nombre = jsonCancion['nombre']
            cancion.ano_lanzamiento = jsonCancion['ano_lanzamiento']
            cancion.duracion = jsonCancion['duracion']
            cancion.save()
            return JsonResponse({"mensaje": "se ha editado correctamente"}, safe=False)
        except Cancion.DoesNotExist:
            return JsonResponse({'error':"No existe la canción"}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def buscarUsuarios(request):

    campos_filtrables = ['nombre', 'apellido', 'email', 'ciudad']

    filtros = {
        f"{campo}__icontains": request.GET.get(campo)
        for campo in campos_filtrables
        if request.GET.get(campo)
    }
    q = Q(**filtros)

    usuarios = Usuario.objects.filter(q).values()
    return JsonResponse(list(usuarios), safe=False)



def buscarUsuariosActivos(request):
    activo_str = request.GET.get('activo')
    filtros = {}

    if activo_str is not None:
        activo = activo_str.lower() == 'true'
        filtros['activo'] = activo

    q = Q(**filtros)
    usuarios = Usuario.objects.filter(q).values()
    return JsonResponse(list(usuarios), safe=False)

@csrf_exempt
def add_usuario(request):
    if request.method == 'POST':
        try:
            jsonUsuario = json.loads(request.body)
            Usuario.objects.create(**jsonUsuario)
            return JsonResponse({"mensaje": "se ha insertado correctamente"}, safe=False,status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': "Error de json desconocido"}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)