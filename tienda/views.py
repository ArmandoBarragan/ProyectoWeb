from django.shortcuts import render
from tienda.models import Categoria, Producto
from tienda.forms import FormCategoria, FormProducto

# Create your views here.
def index(request):
    if request.method == 'POST' and 'submit_producto' in request.POST:
        producto = FormProducto(request.POST)
        if producto.is_valid():
            data = producto.cleaned_data
            data_categoria = data['categoria']
            query_categoria = Categoria.objects.filter(nombre=data_categoria).values()
            categoria = query_categoria[0]
            print(categoria)
            
            nombre = data['nombre']
            precio = data['precio']
            imagen = data['imagen']
            producto_guardado = Producto(
                nombre = nombre,
                precio = precio,
                imagen = imagen,
                categoria = categoria,
            )
            producto_guardado.save()

    if request.method == 'POST' and 'submit_categoria' in request.POST:
        categoria = FormCategoria(request.POST)
        if categoria.is_valid():
            data = categoria.cleaned_data
            nombre = data['nombre']
            categoria_guardada = Categoria(nombre=nombre)
            categoria_guardada.save()



    formProducto = FormProducto()
    formCategoria = FormCategoria()
    productos = Producto.objects.all()

    context = {
        "productos": productos,
        "form_categoria": formCategoria,
        "form_producto": formProducto,
    }
    return render(request, 'tienda.html', context=context)