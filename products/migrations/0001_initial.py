# Generated by Django 3.2 on 2021-08-06 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовка')),
                ('brand', models.CharField(max_length=32, verbose_name='Бренд')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='dashboard/products/', verbose_name='Изброжения')),
                ('first_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='От')),
                ('last_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='До')),
                ('isbn_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Коды товара(ISBN, UPC, GTIN)')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('production', models.BooleanField(default=False, verbose_name='Публикация')),
                ('view', models.IntegerField(default=0, verbose_name='Просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.supercategory', verbose_name='Категория')),
                ('observers', models.ManyToManyField(blank=True, related_name='observers', to=settings.AUTH_USER_MODEL, verbose_name='Студенты')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='dashboard.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Videohosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('body', models.TextField(blank=True, verbose_name='Описание')),
                ('frame_url', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('access', models.BooleanField(default=True, verbose_name='Доступ к видео')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Видеохостинг',
                'verbose_name_plural': 'Видеохостинг',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='Названия')),
                ('value', models.CharField(blank=True, max_length=64, null=True, verbose_name='Значение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='dashboard.supercategory', verbose_name='Категория')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Xарактеристика',
                'verbose_name_plural': 'Xарактеристики',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовка')),
                ('body', models.TextField(blank=True, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('videohosting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.videohosting', verbose_name='Видеохостинг')),
            ],
            options={
                'verbose_name': 'Документация',
                'verbose_name_plural': 'Документации',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300, verbose_name='Тело комментарий')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата написание')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('videohosting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.videohosting', verbose_name='Видеохостинг')),
            ],
            options={
                'verbose_name': 'Комментарии',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dashboard/products/ai/', verbose_name='Изброжения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Дополнительная иллюстрация',
                'verbose_name_plural': 'Дополнительный иллюстрации',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Активность',
                'verbose_name_plural': 'Активности',
            },
        ),
    ]
