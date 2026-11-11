from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProfilUporabnika


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ustvari_profil(sender, instance, created, **kwargs):
    if created:
        ProfilUporabnika.objects.get_or_create(user=instance)