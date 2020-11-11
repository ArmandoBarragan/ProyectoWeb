from django.shortcuts import render
from tienda.models import Categoria, Producto
from tienda.forms import FormCategoria, FormProducto
# Create your views here.
def index(request):
    productos = Producto.objects.all()

    if request.method == 'POST' and 'submit_producto' in request.POST:
        producto = FormProducto(request.POST)
        if producto.is_valid():
            data = producto.cleaned_data
            nombre = data['nombre']
            precio = data['precio']
            categoria = data['categoria']

            if 'imagen' in request.FILES: 
                imagen = request.FILES['imagen']
            else:
                imagen = 'static/media/broken.png'
            producto_guardado = Producto(
                nombre = nombre,
                precio = precio,
                imagen = imagen,
                categoria = categoria,
            )
            producto_guardado.save()

    elif request.method == 'POST' and 'submit_categoria' in request.POST:
        categoria = FormCategoria(request.POST)
        if categoria.is_valid():
            data = categoria.cleaned_data
            nombre = data['nombre']
            categoria_guardada = Categoria(nombre=nombre)
            categoria_guardada.save()

    elif request.method == 'GET' and request.GET.get('busqueda') != None:
        query = request.GET.get('busqueda')
        productos = Producto.objects.filter(nombre__contains=query)

    formProducto = FormProducto()
    formCategoria = FormCategoria()

    context = {
        "productos": productos,
        "form_categoria": formCategoria,
        "form_producto": formProducto,
    }
    return render(request, 'tienda.html', context=context)