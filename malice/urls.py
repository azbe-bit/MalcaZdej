from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.malica_list, name='malica_list'),
    path('malica/<int:pk>/', views.malica_detail, name='malica_detail'),
    path('registracija/', views.registracija, name='register'),
    path('prijava/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('odjava/', auth_views.LogoutView.as_view(), name='logout'),
]