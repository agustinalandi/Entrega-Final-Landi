from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from ropa.models import Pedido
from ropa.forms import Pedido_form
# Create your views here.

def listar_pedidos(request):
    lista_pedidos = Pedido.objects.all()
    context = {'lista_pedidos':lista_pedidos}
    return render(request, 'lista_pedidos.html', context=context)

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def crear_pedido(request):
    if request.method == 'GET':
        form = Pedido_form()
        context = {'form':form}
        return render(request, 'crear_pedido.html', context=context)
    else:
        form = Pedido_form(request.POST)
        if form.is_valid():
            nuevo_pedido = Pedido.objects.create(
                prenda = form.cleaned_data['prenda'],
                precio = form.cleaned_data['precio'],
                fecha_pedido = form.cleaned_data['fecha_pedido'],
            )
            context = {'nuevo_pedido':nuevo_pedido}
        return render(request, 'crear_pedido.html', context=context)

def buscar_pedido(request):
    #pedido = Pedido.objects.get()
    pedidos = Pedido.objects.filter(prenda__icontains = request.GET['search'])
    context = {'pedidos':pedidos}
    return render(request, 'buscar_pedido.html', context = context)
