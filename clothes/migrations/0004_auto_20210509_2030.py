# Generated by Django 3.2 on 2021-05-09 14:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_auto_20210509_1645'),
        ('clothes', '0003_rename_heigth_backpacks_height'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sneakers',
            new_name='Shoes',
        ),
        migrations.AlterModelOptions(
            name='shoes',
            options={'verbose_name': 'Обувь', 'verbose_name_plural': 'Обувь'},
        ),
    ]
