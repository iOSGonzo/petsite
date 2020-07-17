# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pet


# Create your views here.
def home(request):
    return render(request, 'home.html')

def pets_list(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets-list.html', context)

def detail(request, pet_id):
    context = {
        'pet': Pet.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)
