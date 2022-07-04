from multiprocessing import context

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ropa.models import Pedido, Prenda
from ropa.forms import Pedido_form, Prenda_form


# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

class Listar_prendas(ListView):
    model = Prenda
    template_name = 'prendas/lista_prendas.html'
    
class Crear_prenda(LoginRequiredMixin, CreateView):
    model = Prenda
    template_name = 'prendas/crear_prenda.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_prenda', kwargs={'pk':self.object.pk})

class Actualizar_prenda(LoginRequiredMixin, UpdateView):
    model = Prenda
    template_name = 'prendas/actualizar_prenda.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_prenda', kwargs= {'pk':self.object.pk})

class Detallar_prenda(DetailView):
    model = Prenda
    template_name = 'prendas/detalle_prenda.html'

class Eliminar_prenda(LoginRequiredMixin, DeleteView):
    model = Prenda
    template_name = 'prendas/eliminar_prenda.html'

    def get_success_url(self):
        return reverse('listar_prendas')

class Listar_pedidos(ListView):
    model = Pedido
    template_name = 'pedidos/lista_pedidos.html'

class Crear_pedido(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = 'pedidos/crear_pedido.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('detalle_pedido', kwargs={'pk':self.object.pk})

class Actualizar_pedido(LoginRequiredMixin, UpdateView):
    model = Pedido
    template_name = 'pedidos/actualizar_pedido.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_pedido', kwargs= {'pk':self.object.pk})

def buscar_pedido(request):
    #pedido = Pedido.objects.get()
    palabra_buscada = request.GET['search']
    pedidos = Pedido.objects.filter(prenda__icontains = palabra_buscada)
    if pedidos.exists():
        context = {'pedidos': pedidos}
    else: 
        context = {'errors': f'Disculpe, no se encuentra el pedido {palabra_buscada} solicitado.'}
    return render(request, 'buscador.html', context = context)

#def detallar_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
        context = {'pedido':pedido}
        return render(request, 'detalle_pedido.html', context=context)
    except:
        context = {'error':'El pedido no existe'}
        return render(request, 'lista_pedidos.html', context=context)

class Detallar_pedido(DetailView):
    model = Pedido
    template_name = 'pedidos/detalle_pedido.html'

class Eliminar_pedido(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'pedidos/eliminar_pedido.html'

    def get_success_url(self):
        return reverse('lista_pedidos')

