from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Brand
from dashboard.models import Dashboard

@receiver(post_save, sender=Brand)
def create_brand_admin(sender, instance, created, **kwargs):
    if created:
        Dashboard.objects.create(brand=instance)

@receiver(post_save, sender=Brand)
def save_brand_admin(sender, instance, **kwargs):
    instance.dashboard.save()
