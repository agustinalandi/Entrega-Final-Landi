"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ropa.views import index, contacto, Crear_accesorio, Listar_accesorios, Detallar_accesorio, Actualizar_accesorio, Eliminar_accesorio

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('ropa/', include('ropa.urls')),
    path('contacto/', contacto, name = 'contacto'),
    path('crear_accesorio/', Crear_accesorio.as_view(), name = 'crear_accesorio'),
    path('listar_accesorios/', Listar_accesorios.as_view(), name = 'listar_accesorios'),
    path('detalle_accesorio/<int:pk>/', Detallar_accesorio.as_view(), name = 'detalle_accesorio'),
    path('actualizar_accesorio/<int:pk>/', Actualizar_accesorio.as_view(), name = 'actualizar_accesorio'),
    path('eliminar_accesorio/<int:pk>/', Eliminar_accesorio.as_view(), name = 'eliminar_accesorio'),
]


