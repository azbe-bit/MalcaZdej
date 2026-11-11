from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ProfilUporabnika, Sola


class RegistracijaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    sola = forms.ModelChoiceField(
        queryset=Sola.objects.all(), required=False, label="Šola"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "sola"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            profil, _ = ProfilUporabnika.objects.get_or_create(user=user)
            profil.sola = self.cleaned_data.get("sola")
            profil.save()
        return user
