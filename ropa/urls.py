from django.urls import path
from ropa.views import listar_pedidos, crear_pedido, buscar_pedido, crear_prenda

urlpatterns = [
    path('listar_pedidos/', listar_pedidos, name = 'lista_pedidos'),
    path('crear_pedido/', crear_pedido, name = 'crear_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),
    path('crear_prenda/', crear_prenda, name = 'crear_prenda'),
]