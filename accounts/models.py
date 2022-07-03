from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_picture')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return self.name





