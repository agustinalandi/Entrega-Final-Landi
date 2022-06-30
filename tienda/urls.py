from django.contrib import admin
from django.urls import path, include
from ropa.views import index, contacto

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('contacto/', contacto, name = 'contacto'),
    
    path('ropa/', include('ropa.urls')),
    path('accesorios/', include('accesorios.urls')),
    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


