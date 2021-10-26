from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
