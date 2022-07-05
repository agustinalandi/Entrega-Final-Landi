from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    description = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    chosen_url = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'







