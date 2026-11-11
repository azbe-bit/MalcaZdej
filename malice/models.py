from django.conf import settings
from django.db import models


class Sola(models.Model):
    naziv = models.CharField(max_length=150)
    kraj = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Šola"
        verbose_name_plural = "Šole"
        ordering = ["naziv"]

    def __str__(self):
        return f"{self.naziv} ({self.kraj})"


class Malica(models.Model):
    KATEGORIJE = [
        ("topla", "Topla malica"),
        ("hladna", "Hladna malica"),
        ("vegetarijanska", "Vegetarijanska"),
        ("brezglutenska", "Brezglutenska"),
    ]

    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    datum_objave = models.DateTimeField(auto_now_add=True)
    kategorija = models.CharField(max_length=20, choices=KATEGORIJE, blank=True)
    sola = models.ForeignKey(
        Sola, on_delete=models.CASCADE, related_name="malice", null=True, blank=True
    )

    class Meta:
        verbose_name = "Malica"
        verbose_name_plural = "Malice"
        ordering = ["-datum_objave"]

    def __str__(self):
        return self.naziv


class ProfilUporabnika(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sola = models.ForeignKey(
        Sola, on_delete=models.SET_NULL, null=True, blank=True, related_name="profili"
    )

    class Meta:
        verbose_name = "Profil uporabnika"
        verbose_name_plural = "Profili uporabnikov"

    def __str__(self):
        return self.user.username
