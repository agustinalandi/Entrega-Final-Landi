from django.urls import path
from accounts.views import Create_profile, Delete_profile, Detail_profile, Update_profile, View_profile, login_view, logout_view, register_view, user_edit


urlpatterns = [

path('login/', login_view, name = 'login_view'),
path('logout/', logout_view, name = 'logout_view'),
path('sign_up/', register_view, name = 'register_view'),
path('edit_user/', user_edit, name = 'user_edit'),

path('profile/', View_profile.as_view(), name = 'view_profile'),
path('create_profile/<int:pk>/', Create_profile.as_view(), name = 'create_profile'),
path('detail_profile/<int:pk>/', Detail_profile.as_view(), name = 'detail_profile'),
path('update_profile/<int:pk>/', Update_profile.as_view(), name = 'update_profile'),
path('delete_profile/<int:pk>/', Delete_profile.as_view(), name = 'delete_profile'),

] 
