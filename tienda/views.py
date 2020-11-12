from django.shortcuts import render, redirect
from tienda.models import Categoria, Producto
from tienda.forms import FormCategoria, FormProducto
# Create your views here.
def editar(request, id):
    producto = Producto.objects.get(pk=id)
    context = {
        'producto':producto,
        'form_producto': FormProducto(),
    }
    return render(request, 'editarProducto.html', context=context)    

def borrar(request, id):
    producto = Producto.objects.filter(id=id)
    print(producto)

    producto.delete()
    return redirect('index')

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

def update(request, pk):
    producto = Producto.objects.get(pk=pk)
    form_producto = FormProducto(request.POST)
    
    if form_producto.is_valid():
        data = form_producto.cleaned_data
        nombre = data['nombre']
        categoria = data['categoria']
        precio = data['precio']

        if 'imagen' in request.FILES:
            imagen = request.FILES['imagen']
        else:
            imagen = 'static/media/broken.png'

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.imagen = imagen
        producto.save()    

    return redirect('index')