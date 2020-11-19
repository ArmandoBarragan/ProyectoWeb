# from django.shortcuts import render
# from django.urls import path
# # Create your views here.
# def figure(request):
#     context={}
#     return render(request, 'figuras.html', context=context)

# class Rectangulo():
#     #constructor
#     def __init__(self, base, height):
#         #__ inicial significa que es una variable o metodo privado
#         self.__base = base
#         self.__height = height
#         self.__area = self.__calculate_area(base, height)#Los metodos tambien pueden ser privados
#         self.__perimeter = self.__calculate_perimeter(base, height)
    
#     def __calculate_area(self, base, height):
#         return base * height
#     def __calculate_perimeter(self, base, height):
#         return base * 2 + height * 2

#     def get_area(self):
#         return self.area
#     def get_perimeter(self):
#         return self.perimeter

# urlpatterns = [
#     path('figure', figure, name='figure')
# ]