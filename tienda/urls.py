from django.urls import path
from tienda import views

app_name = 'tienda'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/borrar/', views.borrar, name='borrar'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:pk>/update', views.update, name='update')
]

