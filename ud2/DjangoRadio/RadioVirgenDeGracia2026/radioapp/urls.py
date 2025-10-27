#from RadioVirgenDeGracia2026.RadioVirgenDeGracia2026.urls import urlpatterns
from django.urls import path
from . import views
urlpatterns =[
    path('obtenerCancion/<int:id>', views.get_cancion, name="get_cancion"),
    path('addCancion/',views.add_cancion,name="add_cancion"),
    path('obtenerCanciones/', views.get_canciones, name="get_canciones"),
    path('eliminarCancion/<int:id>',views.delete_cancion,name="delete_cancion"),
    path('editarCancion/<int:id>',views.update_cancion,name="update_cancion"),
    path('usuarioClase/',views.buscarUsuarios,name="usuarioClase"),
    path('usuariosActivos/',views.buscarUsuariosActivos),
    path('addUsuario/',views.add_usuario, name='add_usuario'),
]