from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola Mundo')

def simple(request):
    return render(request, 'simple.html')

def dinamico(request, name):
    categories = ['code', 'design', 'marketing'] 
    context = {'name' : name, 'categories': categories}
    return render(request, 'dinamico.html', context)