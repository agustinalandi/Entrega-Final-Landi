from django.contrib import admin
from django.urls import path, include

from accesorios.views import Crear_accesorio, Listar_accesorios, Detallar_accesorio, Actualizar_accesorio, Eliminar_accesorio 


urlpatterns = [

    path('crear_accesorio/', Crear_accesorio.as_view(), name = 'crear_accesorio'),
    path('listar_accesorios/', Listar_accesorios.as_view(), name = 'listar_accesorios'),
    path('detalle_accesorio/<int:pk>/', Detallar_accesorio.as_view(), name = 'detalle_accesorio'),
    path('actualizar_accesorio/<int:pk>/', Actualizar_accesorio.as_view(), name = 'actualizar_accesorio'),
    path('eliminar_accesorio/<int:pk>/', Eliminar_accesorio.as_view(), name = 'eliminar_accesorio'),

] 

