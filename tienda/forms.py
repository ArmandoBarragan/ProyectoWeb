from django import forms
from tienda.models import Categoria, Producto

class FormCategoria(forms.ModelForm):
    class Meta:
        model =  Categoria
        fields = ['nombre']

class FormProducto(forms.ModelForm):    
    class Meta:
        model = Producto

        fields = ['nombre', 'categoria', 'precio', 'imagen']
    
    

