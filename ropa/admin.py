from django.contrib import admin
from ropa.models import Accesorio, Pedido, Prenda

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Prenda)
admin.site.register(Accesorio)
