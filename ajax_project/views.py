from django.shortcuts import render
from django import forms
from .models import Person
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'job', 'salary']

def index(request):
    if request.method == "POST":
        form = PersonForm(data=request.POST)
        form.save()
    
    context = {
        'form': PersonForm()
    }
    return render(request, 'ajax/search.html', context=context)

def search(request):
    if request.method == "GET":
        try:
            name = request.GET.get('name')
            query = Person.objects.filter(name__startswith=name)
            people = [people_serializer(person) for person in query]
            print(people)

            return HttpResponse(json.dumps(people), content_type='application/json')

        except ValueError as error:
            return HttpResponse(error)

def people_serializer(person):
    data = {
        'name':person.name,
        'last_name': person.last_name,
        'job': person.job,
        'salary': person.salary,
    }
    return data
