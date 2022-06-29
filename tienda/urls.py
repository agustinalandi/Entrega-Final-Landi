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
from ropa.views import cargar_accesorio, contacto, index, Listar_accesorios, detallar_accesorio, eliminar_accesorio

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('ropa/', include('ropa.urls')),
    path('contacto/', contacto, name = 'contacto'),
    path('listar_accesorios/', Listar_accesorios.as_view(), name = 'listar_accesorios'),
    path('cargar_accesorio/', cargar_accesorio, name = 'cargar_accesorio'),
    path('detalle_accesorio/<int:pk>/', detallar_accesorio, name = 'detalle_accesorio'),
    path('eliminar_accesorio/<int:pk>/', eliminar_accesorio, name = 'eliminar_accesorio'),
]
