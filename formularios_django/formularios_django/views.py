from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm

def form(request):
  comment_form = CommentForm({'name': 'Jairo', 'url': 'http://open-bootcamp.com', 'comment': 'Comentario'})
  return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
  if request.method != 'POST':
    return HttpResponse('Método no permitodo')

  return HttpResponse(request.POST['name'])