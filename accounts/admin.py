from django.contrib import admin
from accounts.models import User_profile

#admin.site.register(User_profile)

@admin.register(User_profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'phone', 'profile_picture', 'chosen_url']