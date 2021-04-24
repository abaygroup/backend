# Generated by Django 3.2 on 2021-04-24 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logotype', models.ImageField(blank=True, null=True, upload_to='dashboard/avatar/', verbose_name='Логотип')),
                ('branch', models.CharField(choices=[('BEAUTY', 'Красота'), ('CLOTHES', 'Одежда'), ('ELECTRONICS', 'Электроника'), ('FURNIURE', 'Мебель'), ('CRAFTS', 'Ремесла'), ('JEWERLY', 'Ювелирные украшения'), ('PICTURE', 'Картина'), ('PHOTO', 'Фотография'), ('RESTAURANTS', 'Рестораны'), ('FOOD_PRODUCTS', 'Продовольственные товары'), ('OTHER_FOOD_AND_DRINKS', 'Другая еда и напитки'), ('SPORTING', 'Спортивный'), ('TOYS', 'Игрушки'), ('SERVICES', 'Услуги'), ('VIRTUAL_SERVICES', 'Виртуальные сервисы'), ('ANOTHER', 'Другой'), ('I_HAVEN_NOT_DECIDED_YET', 'Я еще не решил')], default='I_HAVEN_NOT_DECIDED_YET', max_length=50, verbose_name='Отрасль')),
                ('body', models.TextField(blank=True, max_length=300, null=True, verbose_name='О вас')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ваше имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ваше фамилия')),
                ('gender', models.CharField(choices=[('N', 'Не указано'), ('M', 'Мужской'), ('F', 'Женский')], default='Не указано', max_length=1, verbose_name='Пол')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Контакт телефона', max_length=31, verbose_name='Телефон')),
                ('city', models.CharField(choices=[('ALMATY', 'Алматы'), ('NURSULTAN', 'Нұр-Сұлтан'), ('SHYMKENT', 'Шымкент'), ('AQTOBE', 'Ақтөбе'), ('QARAGANDY', 'Қарағанды'), ('TARAZ', 'Тараз'), ('PAVLODAR', 'Павлодар'), ('OSKEMEN', 'Өскемен'), ('SEMEI', 'Семей'), ('ATYRAU', 'Атырау'), ('QOSTANAI', 'Қостанай'), ('QYZYLORDA', 'Қызылорда'), ('ORAL', 'Орал'), ('PETROPAVL', 'Петропавл'), ('AQTAU', 'Ақтау'), ('TEMYRTAU', 'Теміртау'), ('KOKSHETAU', 'Көкшетау'), ('TALDYQORGAN', 'Талдықорған'), ('EKYBASTUZ', 'Екібастұз'), ('RUDNY', 'Рудный'), ('ZHANAOZEN', 'Жаңаөзен'), ('BALQASH', 'Балқаш'), ('KENTAU', 'Кентау'), ('QASKELEN', 'Қаскелең'), ('SATBAEV', 'Сәтбаев'), ('QULSARY', 'Құлсары')], default='ALMATY', max_length=255, verbose_name='Город')),
                ('reserve_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Резервный email')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Веб сайт')),
                ('branding', models.BooleanField(default=False, verbose_name='Брендинг')),
                ('for_clients', models.BooleanField(default=False, verbose_name='Вы открываете это для клиента?')),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Панель управление',
                'verbose_name_plural': 'Панели управление',
            },
        ),
    ]
