from django.urls import path
from accounts.views import login_view, logout_view, register_view

urlpatterns = [

path('login/', login_view, name = 'login_view'),
path('logout/', logout_view, name = 'logout_view'),
path('sign_up/', register_view, name = 'register_view')

]
