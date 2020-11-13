from django.shortcuts import render
from django import forms
from .models import Person
# Create your views here.
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'job', 'salary']

def ajax_search(request):
    context = {
        'form': PersonForm()
    }
    
    return render(request, 'ajax/search.html', context=context)

