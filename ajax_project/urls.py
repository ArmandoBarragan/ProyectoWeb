from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='ajax_index'),
    path('search/', views.search, name='ajax_search')
]