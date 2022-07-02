from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accesorios.models import Accesorio
from accesorios.forms import Accesorio_form

class Listar_accesorios(ListView):
    model = Accesorio
    template_name = 'lista_accesorios.html'

class Crear_accesorio(LoginRequiredMixin, CreateView):
    model = Accesorio
    template_name = 'crear_accesorio.html'
    fields = ['tipo', 'color', 'es_resistente_agua', 'precio']
    
    def get_success_url(self):
        return reverse('detalle_accesorio', kwargs={'pk':self.object.pk})

class Actualizar_accesorio(LoginRequiredMixin, UpdateView):
    model = Accesorio
    template_name = 'actualizar_accesorio.html'
    fields = ['tipo', 'color', 'es_resistente_agua', 'precio']

    def get_success_url(self):
        return reverse('detalle_accesorio', kwargs= {'pk':self.object.pk})

class Detallar_accesorio(DetailView):
    model = Accesorio
    template_name = 'detalle_accesorio.html'

class Eliminar_accesorio(LoginRequiredMixin, DeleteView):
    model = Accesorio
    template_name = 'eliminar_accesorio.html'

    def get_success_url(self):
        return reverse('listar_accesorios')

