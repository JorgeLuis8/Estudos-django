from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request,'sobre.html')

def contact(request):
    return render(request,'contato.html')