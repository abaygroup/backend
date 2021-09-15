# Generated by Django 3.2 on 2021-09-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_author'),
        ('products', '0009_alter_videohosting_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='dashboard.Author'),
        ),
    ]
