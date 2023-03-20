from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse("Sobre")

def contact(request):
    return HttpResponse("Contact")