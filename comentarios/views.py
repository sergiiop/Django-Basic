from calendar import c
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Comment

# Create your views here.

def test(request):
    return HttpResponse('Hello world')

#crear un comentario
def create(request):
    # crear un objeto apartir de un modelo
    # comment = Comment(name='Sergio', score=5, comment='Este es un comentario')
    # guardar el objeto en la base de datos
    # comment.save()

    #Crea el objeto apartir del modelo y lo guarda
    comment = Comment.objects.create(name='akira')
    return HttpResponse('creada')

def delete(request):
    #obtener el objeto con id = 1
    # comment = Comment.objects.get(id=1)
    #eliminar el objeto obtenido
    # comment.delete()

    Comment.objects.filter(id=2).delete()
    return HttpResponse('deleted')