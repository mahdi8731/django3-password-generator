from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, "generator/about.html")


def password(request):
    thepassword = ""

    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('UperCase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special'):
        characters.extend("!@#$%&*")
    if request.GET.get('numbers'):
        characters.extend("0123456789")
    lenght = int(request.GET.get('length', 10))

    for x in range(0, lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
