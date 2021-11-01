# Generated by Django 3.2 on 2021-10-23 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, help_text='Максимальный размер файла 2MB', null=True, upload_to='profile/authors/', validators=[profile.models.Author.validate_picture])),
                ('full_name', models.CharField(max_length=64, verbose_name='Полная имя автора')),
                ('about', models.TextField(verbose_name='О авторе')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Ключовой адрес')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/categories/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Тема')),
                ('body', models.TextField(verbose_name='Описание')),
                ('date_send', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправление')),
                ('checked', models.BooleanField(default=False, verbose_name='Проверка')),
                ('from_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кому')),
                ('to_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_to', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомлений',
                'ordering': ['-date_send'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегорий',
                'ordering': ('super_category__name', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profile.category',),
        ),
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
            ],
            options={
                'verbose_name': 'Надкатегория',
                'verbose_name_plural': 'Надкатегорий',
                'ordering': ('name',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profile.category',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, help_text='Максимальный размер файла 2MB', null=True, upload_to='profile/avatar/', validators=[profile.models.Profile.validate_logotype], verbose_name='Аватар')),
                ('body', models.TextField(blank=True, max_length=300, null=True, verbose_name='О вас')),
                ('address', models.TextField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('branding', models.BooleanField(default=False, verbose_name='Брендинг')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profile.supercategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profile.supercategory', verbose_name='Надкатегория'),
        ),
    ]