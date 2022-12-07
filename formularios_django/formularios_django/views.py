from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def form(request):
  comment_form = CommentForm({'name': 'Jairo', 'url': 'http://open-bootcamp.com', 'comment': 'Comentario'})
  return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
  if request.method != 'POST':
    return HttpResponse('Método no permitodo')

  return HttpResponse(request.POST['name'])

def widget(request):
  if request.method == 'GET':
    form = ContactForm()
    return render(request, 'widget.html', {'form': form})

  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      #? Todas las acciones a realizar cuando los datos son conrrectos
      return HttpResponse('Válido')
    else:
      #? Comunicamos al usuario que los datos no son válidos
      return render(request, 'widget.html', {'form': form})