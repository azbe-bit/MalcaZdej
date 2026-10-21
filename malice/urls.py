from django.urls import path
from .views import seznam_malic, prijava_view, odjava_view

urlpatterns = [
    path('', seznam_malic, name='seznam_malic'),
    path('prijava/', prijava_view, name='prijava'),
    path('odjava/', odjava_view, name='odjava'), # <-- Tukaj uporabiva najino funkcijo
]