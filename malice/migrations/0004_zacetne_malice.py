from pathlib import Path

from django.core.files import File
from django.db import migrations

SLIKE_DIR = Path(__file__).resolve().parent.parent / "seed_slike"

MALICE = [
    {
        "naziv": "Domači dunajec z rahlim pirejem",
        "opis": (
            "Okus otroštva na enem krožniku! Sočen in hrustljav zrezek, pripravljen po "
            "tradicionalnem receptu, v kombinaciji z ročno pripravljenim, bogatim "
            "krompirjevim pirejem. Preprosto, pošteno in izjemno okusno."
        ),
        "cena": "7.49",
        "kategorija": "topla",
        "slika": "",
    },
    {
        "naziv": "Čufti",
        "opis": "SEM PRILEPI CEL OPIS IZ ADMINA",
        "cena": "6.67",
        "kategorija": "topla",
        "slika": "svaljki.jpg",
    },
]


def dodaj_malice(apps, schema_editor):
    Malica = apps.get_model("malice", "Malica")

    for podatki in MALICE:
        malica, _ = Malica.objects.get_or_create(
            naziv=podatki["naziv"],
            defaults={
                "opis": podatki["opis"],
                "cena": podatki["cena"],
                "kategorija": podatki["kategorija"],
            },
        )
        ime_slike = podatki.get("slika")
        if ime_slike and not malica.slika:
            pot = SLIKE_DIR / ime_slike
            if pot.exists():
                with open(pot, "rb") as f:
                    malica.slika.save(ime_slike, File(f), save=True)


class Migration(migrations.Migration):

    dependencies = [
        ("malice", "0003_alter_malica_options_alter_profiluporabnika_options_and_more"),
    ]

    operations = [
        migrations.RunPython(dodaj_malice, migrations.RunPython.noop),
    ]