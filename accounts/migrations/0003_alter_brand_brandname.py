# Generated by Django 3.2 on 2021-09-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210826_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brandname',
            field=models.CharField(max_length=32, unique=True, verbose_name='имя пользователя'),
        ),
    ]
