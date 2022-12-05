from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

def update(request):
  author = Author.objects.get(id=1)
  author.name = 'Jairo'
  author.email = 'jairo@demoexample.com'
  author.save()
  return HttpResponse('Modificado')

def queries(request):
  # Obtener todos los elementos
  authors = Author.objects.all()

  #? Obtener los datos por condición
  filtered = Author.objects.filter(email='nicole36@example.net')

  # Obtener un único objeto
  author = Author.objects.get(id=1)

  #? Obtener los 10 primeros elementos
  limits = Author.objects.all()[:10]

  # Obtener los 5 elementos saltando los 5 primeros
  offsets = Author.objects.all()[5:10]

  #? Obtener todos los elementos ordenados
  orders = Author.objects.all().order_by('email')

  # Obtener todos los elementos de id menor o igual a 15
  filtered2 = Author.objects.filter(id__lte=15)

  #? Obtener todos los autores que consitenen en su nombre la palabra (yes)
  contained = Author.objects.filter(name__contains='new')

  return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtered2': filtered2, 'contained': contained})