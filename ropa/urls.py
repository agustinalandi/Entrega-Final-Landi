from django.urls import path
from ropa.views import detallar_pedido, eliminar_prenda, Listar_pedidos, crear_pedido, buscar_pedido, crear_prenda, Listar_prendas, detallar_prenda, eliminar_pedido

urlpatterns = [
    path('listar_pedidos/', Listar_pedidos.as_view(), name = 'lista_pedidos'),
    path('crear_pedido/', crear_pedido, name = 'crear_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),
    path('crear_prenda/', crear_prenda, name = 'crear_prenda'),
    path('listar_prendas/', Listar_prendas.as_view(), name = 'listar_prendas'),
    path('detalle_prenda/<int:pk>/', detallar_prenda, name = 'detalle_prenda'),
    path('eliminar_prenda/<int:pk>/', eliminar_prenda, name = 'eliminar_prenda'),
    path('detalle_pedido/<int:pk>/', detallar_pedido, name = 'detalle_pedido'),
    path('eliminar_pedido/<int:pk>/', eliminar_pedido, name = 'eliminar_pedido'),
]