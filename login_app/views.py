from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path, include
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def login(request):    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                do_login(request,user)
                return redirect('home')
            
    context = {
        'form': AuthenticationForm(),
    }
    return render (request, 'auth/login.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            do_login(request, user)

            return redirect('home')
   
    context = {
        'form': UserCreationForm()
    }
    
    return render(request, 'auth/register.html', context)

def home(request):
    if request.user.is_authenticated:
        return render(request, 'auth/home.html', {'user': request.user})
    return HttpResponse("No tienes permiso de estar aquí, bro")

def logout(request):
    do_logout(request)
    return redirect('login')

app_name = 'login'
urlpatterns = [
    path('', login, name='login'),
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('logout', logout, name='logout')
]