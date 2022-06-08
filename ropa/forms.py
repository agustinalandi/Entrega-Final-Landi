from django import forms
from ropa.models import Accesorio, Pedido, Prenda

# class Pedido_form(forms.Form):
#    prenda = forms.CharField(max_length=100)
#    precio = forms.FloatField()
#    fecha_pedido = forms.DateField()

class Pedido_form(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class Prenda_form(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = '__all__'

class Accesorio_form(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = '__all__'

