from django import forms
from tienda.models import Categoria

class FormCategoria(forms.ModelForm):
    class Meta:
        model =  Categoria
        fields = ['nombre']

class FormProducto(forms.Form):
    choices = []
    categorias = Categoria.objects.all()
    
    for categoria in categorias:
        nombre = categoria.nombre
        tupla = (nombre, nombre)
        choices.append(tupla)
    
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    categoria = forms.ChoiceField(choices=choices)
    imagen = forms.ImageField(required=False)



