from django.db import models
from django.contrib.auth.models import User

class Sola(models.Model):
    naziv = models.CharField(max_length=150)
    kraj = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.naziv} ({self.kraj})"

class ProfilUporabnika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sola = models.ForeignKey(Sola, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.sola}"

class Malica(models.Model):
    KATEGORIJE = [
        ('topla', 'Topla malica'),
        ('hladna', 'Hladna malica'),
        ('veganski', 'Veganski menu'),
        ('pijaca', 'Pijača in prigrizek'),
    ]
    
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    kategorija = models.CharField(max_length=20, choices=KATEGORIJE, default='topla')  # <-- POPRAVLJENO IZ max_digits V max_length
    sola = models.ForeignKey(Sola, on_delete=models.CASCADE, null=True, blank=True)
    datum_objave = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naziv} ({self.cena} €)"