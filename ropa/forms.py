from django import forms
from ropa.models import Pedido

# class Pedido_form(forms.Form):
#    prenda = forms.CharField(max_length=100)
#    precio = forms.FloatField()
#    fecha_pedido = forms.DateField()

class Pedido_form(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
