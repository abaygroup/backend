from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    verbose_name = 'Панель управление'
    verbose_name_plural = 'Панели управления'
