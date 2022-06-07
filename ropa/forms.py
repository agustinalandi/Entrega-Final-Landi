from django import forms

class Pedido_form(forms.Form):
    prenda = forms.CharField(max_length=100)
    precio = forms.FloatField()
    fecha_pedido = forms.DateField()