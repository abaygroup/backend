# Generated by Django 3.2 on 2021-08-28 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210826_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docs',
            name='videohosting',
        ),
        migrations.DeleteModel(
            name='AdditionalImage',
        ),
        migrations.DeleteModel(
            name='Docs',
        ),
    ]
