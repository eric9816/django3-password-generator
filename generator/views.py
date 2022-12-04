from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend([i.upper() for i in characters])
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend([str(i) for i in range(0, 10)])
    lenght = int(request.GET.get('length', 12))  # берется из html файла

    password = ''
    for i in range(lenght):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

def author(request):
    return render(request, 'generator/author.html')
