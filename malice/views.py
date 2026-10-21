from django.shortcuts import render
from .models import Malica

def seznam_malic(request):
    malice = Malica.objects.all()
    return render(request, 'malice/seznam.html', {'malice': malice})