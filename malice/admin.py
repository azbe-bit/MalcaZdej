from django.contrib import admin

from .models import Malica, ProfilUporabnika, Sola


@admin.register(Sola)
class SolaAdmin(admin.ModelAdmin):
    list_display = ("naziv", "kraj")
    search_fields = ("naziv", "kraj")


@admin.register(Malica)
class MalicaAdmin(admin.ModelAdmin):
    list_display = ("naziv", "sola", "kategorija", "cena", "datum_objave")
    list_filter = ("kategorija", "sola")
    search_fields = ("naziv", "opis")


@admin.register(ProfilUporabnika)
class ProfilUporabnikaAdmin(admin.ModelAdmin):
    list_display = ("user", "sola")
    list_filter = ("sola",)
