from django.apps import AppConfig


class MaliceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'malice'
    verbose_name = 'Malice'

    def ready(self):
        import malice.signals  # noqa: F401
