from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from ropa.models import Pedido, Prenda, Accesorio
from ropa.forms import Pedido_form, Prenda_form, Accesorio_form

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def listar_prendas(request):
    lista_prendas = Prenda.objects.all()
    context = {'lista_prendas':lista_prendas}
    return render(request, 'lista_prendas.html', context=context)

def listar_pedidos(request):
    lista_pedidos = Pedido.objects.all()
    context = {'lista_pedidos':lista_pedidos}
    return render(request, 'lista_pedidos.html', context=context)

def listar_accesorios(request):
    lista_accesorios = Accesorio.objects.all()
    context = {'lista_accesorios':lista_accesorios}
    return render(request, 'lista_accesorios.html', context=context)

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
                es_temporada_actual = form.cleaned_data['es_temporada_actual'],
            )
            context = {'nuevo_pedido': nuevo_pedido}
        #else:
        #    context = {'errors': form.errors}
        return render(request, 'crear_pedido.html', context=context)

def buscar_pedido(request):
    #pedido = Pedido.objects.get()
    palabra_buscada = request.GET['search']
    pedidos = Pedido.objects.filter(prenda__icontains = palabra_buscada)
    if pedidos.exists():
        context = {'pedidos': pedidos}
    else: 
        context = {'errors': f'Disculpe, no se encuentra el pedido {palabra_buscada} solicitado.'}
    return render(request, 'buscador.html', context = context)

def crear_prenda(request):
    if request.method == 'GET':
        form = Prenda_form()
        context = {'form':form}
        return render(request, 'crear_prenda.html', context=context)
    else:
        form = Prenda_form(request.POST)
        if form.is_valid():
            nueva_prenda = Prenda.objects.create(
                nombre = form.cleaned_data['nombre'],
                talle = form.cleaned_data['talle'],
                color = form.cleaned_data['color'],
            )
            context = {'nueva_prenda': nueva_prenda}
        #else:
        #    context = {'errors': form.errors}
        return render(request, 'crear_prenda.html', context=context)

def cargar_accesorio(request):
    if request.method == 'GET':
        form = Accesorio_form()
        context = {'form':form}
        return render(request, 'cargar_accesorio.html', context=context)
    else:
        form = Accesorio_form(request.POST)
        if form.is_valid():
            nuevo_accesorio = Accesorio.objects.create(
                tipo = form.cleaned_data['tipo'],
                talle_accesorio = form.cleaned_data['talle_accesorio'],
                color_accesorio = form.cleaned_data['color_accesorio'],
                es_para_regalo = form.cleaned_data['es_para_regalo'],
            )
            context = {'nuevo_accesorio': nuevo_accesorio}
        #else:
        #    context = {'errors': form.errors}
        return render(request, 'cargar_accesorio.html', context=context)

