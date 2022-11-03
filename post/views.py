from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados por condicion, obtenemos una colecction con filter
    filtered = Author.objects.filter(email='tranannette@example.org')

    # Obtener un unico objeto
    author = Author.objects.get(id=1)

    #Obtener los primeros 10 elementos
    limit = Author.objects.all()[:10]

    # Obtener 5 valores saltando los 5 primeros
    offset = Author.objects.all()[5:10]

    return render(request, 'post/queries.html', {
        'authors': authors,
        'filtered': filtered,
        'author': author,
        'limit': limit,
        'offset': offset
    })

# Create your views here.
