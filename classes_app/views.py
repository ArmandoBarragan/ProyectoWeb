from django.shortcuts import render
from django.urls import path
# Create your views here.
def figure(request):
    rect = Rectangle(10,15)
    context={
        'base': rect.base,
        'height': rect.height,
        'area': rect.get_area(),
        'perimeter': rect.get_perimeter(),
        }
    return render(request, 'figuras.html', context=context)

class Rectangle():
    #constructor
    def __init__(self, base, height):
        #__ inicial significa que es una variable o metodo privado
        self.base = base
        self.height = height
        self.__area = self.__calculate_area(base, height)#Los metodos tambien pueden ser privados
        self.__perimeter = self.__calculate_perimeter(base, height)
    
    def __calculate_area(self, base, height):
        return base * height
    def __calculate_perimeter(self, base, height):
        return base * 2 + height * 2

    def get_area(self):
        return self.__area
    def get_perimeter(self):
        return self.__perimeter

urlpatterns = [
    path('figure', figure, name='figure')
]