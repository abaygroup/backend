# Generated by Django 3.2 on 2021-08-26 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_favorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Избранный', 'verbose_name_plural': 'Избранные'},
        ),
    ]