from django.shortcuts import render
from .forms import EmployeesForm

def index(request):
  form = EmployeesForm()
  return render(request, 'index.html', {'form': form})