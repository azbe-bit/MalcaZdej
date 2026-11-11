from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistracijaForm
from .models import Malica, Sola


def registracija(request):
    if request.user.is_authenticated:
        return redirect('malica_list')

    if request.method == 'POST':
        form = RegistracijaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('malica_list')
    else:
        form = RegistracijaForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def malica_list(request):
    profil = getattr(request.user, 'profiluporabnika', None)
    sola = profil.sola if profil else None

    malice = Malica.objects.select_related('sola').all()
    if sola:
        malice = malice.filter(sola=sola)

    kategorija = request.GET.get('kategorija')
    if kategorija:
        malice = malice.filter(kategorija=kategorija)

    context = {
        'malice': malice,
        'sola': sola,
        'kategorije': Malica.KATEGORIJE,
        'izbrana_kategorija': kategorija,
    }
    return render(request, 'malica/malica_list.html', context)


@login_required
def malica_detail(request, pk):
    malica = get_object_or_404(Malica, pk=pk)
    return render(request, 'malica/malica_detail.html', {'malica': malica})