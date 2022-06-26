from django.urls import path
from ropa.views import listar_pedidos, crear_pedido, buscar_pedido, crear_prenda, listar_prendas

urlpatterns = [
    path('listar_pedidos/', listar_pedidos, name = 'lista_pedidos'),
    path('crear_pedido/', crear_pedido, name = 'crear_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),
    path('crear_prenda/', crear_prenda, name = 'crear_prenda'),
    path('listar_prendas/', listar_prendas, name = 'listar_prendas'),
]