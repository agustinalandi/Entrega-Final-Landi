from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message': f'Bienvenido {username} a la Tienda'}
                return render(request, 'index.html', context=context)
            else:
                form = AuthenticationForm()
                context = {'error':'No hay ningun usuario con esas credenciales.'}
                return render(request, 'login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'login.html', context=context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context=context)
