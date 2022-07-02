from django import forms
from accesorios.models import Accesorio

class Accesorio_form(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = '__all__'
        