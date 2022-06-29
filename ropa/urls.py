from django.urls import path
from ropa.views import Detallar_pedido, eliminar_prenda, Listar_pedidos, Crear_pedido, buscar_pedido, Crear_prenda, Listar_prendas, Detallar_prenda, eliminar_pedido

urlpatterns = [
    path('listar_pedidos/', Listar_pedidos.as_view(), name = 'lista_pedidos'),
    path('crear_pedido/', Crear_pedido.as_view(), name = 'crear_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),
    path('crear_prenda/', Crear_prenda.as_view(), name = 'crear_prenda'),
    path('listar_prendas/', Listar_prendas.as_view(), name = 'listar_prendas'),
    path('detalle_prenda/<int:pk>/', Detallar_prenda.as_view(), name = 'detalle_prenda'),
    path('eliminar_prenda/<int:pk>/', eliminar_prenda, name = 'eliminar_prenda'),
    path('detalle_pedido/<int:pk>/', Detallar_pedido.as_view(), name = 'detalle_pedido'),
    path('eliminar_pedido/<int:pk>/', eliminar_pedido, name = 'eliminar_pedido'),
]
