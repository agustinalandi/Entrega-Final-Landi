from django.db import models

class Accesorio(models.Model):
    tipo = models.CharField(max_length=50)
    talle_accesorio = models.IntegerField()
    color_accesorio = models.CharField(max_length=70)
    es_para_regalo = models.BooleanField(default=True)
    imagen_accesorio = models.ImageField(upload_to='imagenes_accesorios')

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'
