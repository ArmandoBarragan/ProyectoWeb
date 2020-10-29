from django import forms
from tienda.models import Categoria, Producto

class FormCategoria(forms.ModelForm):
    class Meta:
        model =  Categoria
        fields = ['nombre']

class FormProducto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormProducto, self).__init__(*args, **kwargs)
        
        categorias = Categoria.objects.all()
        choices=[]

        for categoria in categorias:
            nombre = categoria.nombre
            tupla = (nombre, nombre)
            choices.append(tupla)

        self.fields['categoria'] = forms.ChoiceField(choices=choices)
    
    class Meta:
        model = Producto

        fields = ['nombre', 'categoria', 'precio', 'imagen']
    
    # def __init__(self, *args, **kwards):
    #     super(FormProducto, self).__init__(*args, **kwards)
    #     choices = []
    #     categorias = Categoria.objects.all()
        
    #     for categoria in categorias:
    #         nombre = categoria.nombre
    #         tupla = (nombre, nombre)
    #         choices.append(tupla)
        
    #     self.nombre = forms.CharField(max_length=100)
    #     self.precio = forms.DecimalField(max_digits=10, decimal_places=2)
    #     self.categoria = forms.ChoiceField(choices=choices)
    #     self.imagen = forms.ImageField(required=False)

    

