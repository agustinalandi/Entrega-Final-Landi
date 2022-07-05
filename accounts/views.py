from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from accounts.forms import User_registration_form, User_edit_form
from accounts.models import User_profile


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
                return render(request, 'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context=context)

def logout_view(request):
    logout(request)
    return render(request, 'index.html')
    #return redirect('index.html')

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context = {'message':f'Usuario creado con exito, bienvenido {username}'}
            return render(request, 'index.html', context=context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context=context)
    else:
        form = User_registration_form
        context = {'form':form}
        return render(request, 'auth/register.html', context=context)

def user_edit(request):
    user = request.user
    if request.method == 'POST':
        form = User_edit_form(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.password1 = form.cleaned_data['password1']
            user.password2 = form.cleaned_data['password2']
            user.save()
            context = {'message':'Usuario editado con exito.'}
            return render(request, 'index.html', context=context)
    else:
        form = User_edit_form(initial={'email':user.email})
    return render(request, 'auth/edit_user.html', {'form':form, 'user':user})

class Create_profile(LoginRequiredMixin, CreateView):
    model = User_profile
    template_name = 'auth/create_profile.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('view_profile', kwargs={'pk':self.object.pk})

class Detail_profile(DetailView):
    model = User_profile
    template_name = 'auth/detail_profile.html'

class Update_profile(LoginRequiredMixin, UpdateView):
    model = User_profile
    template_name = 'auth/update_profile.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_profile', kwargs= {'pk':self.object.pk})

class View_profile(ListView):
    model = User_profile
    template_name = 'auth/profile.html'

class Delete_profile(LoginRequiredMixin, DeleteView):
    model = User_profile
    template_name = 'auth/delete_profile.html'

    def get_success_url(self):
        return reverse('view_profile')
