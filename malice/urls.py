from django.urls import path
from .views import seznam_malic

urlpatterns = [
    path('', seznam_malic, name='seznam_malic'),
]