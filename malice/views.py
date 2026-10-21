from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import Malica, ProfilUporabnika
from django.contrib.auth import logout

def seznam_malic(request):
    sola_uporabnika = None
    if request.user.is_authenticated:
        try:
            profil = ProfilUporabnika.objects.get(user=request.user)
            sola_uporabnika = profil.sola
        except ProfilUporabnika.DoesNotExist:
            pass

    if sola_uporabnika:
        malice = Malica.objects.filter(sola=sola_uporabnika) | Malica.objects.filter(sola__isnull=True)
    else:
        malice = Malica.objects.all()

    return render(request, 'malice/seznam.html', {
        'malice': malice,
        'sola_uporabnika': sola_uporabnika
    })

def prijava_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('seznam_malic')
    else:
        form = AuthenticationForm()
    return render(request, 'malice/prijava.html', {'form': form})

def odjava_view(request):
    logout(request)
    return redirect('prijava')