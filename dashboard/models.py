from django.db import models
from accounts.models import Brand
from phone_field import PhoneField
import uuid


# Модель Adminstore
class Dashboard(models.Model):
    class CityType(models.TextChoices):
        ALMATY = 'ALMATY', 'Алматы'
        NURSULTAN = 'NURSULTAN', 'Нұр-Сұлтан'
        SHYMKENT = 'SHYMKENT', 'Шымкент'
        AQTOBE = 'AQTOBE', 'Ақтөбе'
        QARAGANDY = 'QARAGANDY', 'Қарағанды'
        TARAZ = 'TARAZ', 'Тараз'
        PAVLODAR = 'PAVLODAR', 'Павлодар'
        OSKEMEN = 'OSKEMEN', 'Өскемен'
        SEMEI = 'SEMEI', 'Семей'
        ATYRAU = 'ATYRAU', 'Атырау'
        QOSTANAI = 'QOSTANAI', 'Қостанай'
        QYZYLORDA = 'QYZYLORDA', 'Қызылорда'
        ORAL = 'ORAL', 'Орал'
        PETROPAVL = 'PETROPAVL', 'Петропавл'
        AQTAU = 'AQTAU', 'Ақтау'
        TEMYRTAU = 'TEMYRTAU', 'Теміртау'
        KOKSHETAU = 'KOKSHETAU', 'Көкшетау' 
        TALDYQORGAN = 'TALDYQORGAN', 'Талдықорған' 
        EKYBASTUZ = 'EKYBASTUZ', 'Екібастұз' 
        RUDNY = 'RUDNY', 'Рудный' 
        ZHANAOZEN = 'ZHANAOZEN', 'Жаңаөзен' 
        BALQASH = 'BALQASH', 'Балқаш' 
        KENTAU = 'KENTAU', 'Кентау' 
        QASKELEN = 'QASKELEN', 'Қаскелең' 
        SATBAEV = 'SATBAEV', 'Сәтбаев' 
        QULSARY = 'QULSARY', 'Құлсары' 

    class Branch(models.TextChoices):
        BEAUTY = 'BEAUTY', 'Красота'
        CLOTHES = 'CLOTHES', 'Одежда'
        ELECTRONICS = 'ELECTRONICS', 'Электроника'
        FURNIURE = 'FURNIURE', 'Мебель'
        CRAFTS = 'CRAFTS', 'Ремесла'
        JEWERLY = 'JEWERLY', 'Ювелирные украшения'
        PICTURE = 'PICTURE', 'Картина'
        PHOTO = 'PHOTO', 'Фотография'
        RESTAURANTS = 'RESTAURANTS', 'Рестораны'
        FOOD_PRODUCTS = 'FOOD_PRODUCTS', 'Продовольственные товары'
        OTHER_FOOD_AND_DRINKS = 'OTHER_FOOD_AND_DRINKS', 'Другая еда и напитки'
        SPORTING = 'SPORTING', 'Спортивный'
        TOYS = 'TOYS', 'Игрушки'
        SERVICES = 'SERVICES', 'Услуги'
        VIRTUAL_SERVICES = 'VIRTUAL_SERVICES', 'Виртуальные сервисы'
        ANOTHER = 'ANOTHER', 'Другой'
        I_HAVEN_NOT_DECIDED_YET = 'I_HAVEN_NOT_DECIDED_YET', 'Я еще не решил' 

    GENDER_CHOICES = (
        ('N', 'Не указано'),
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    # Направление бренда или магазина
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    logotype = models.ImageField(verbose_name='Логотип', upload_to='dashboard/avatar/', blank=True, null=True)
    branch = models.CharField(verbose_name='Отрасль', max_length=50, choices=Branch.choices, default=Branch.I_HAVEN_NOT_DECIDED_YET)
    body = models.TextField(verbose_name='О вас', max_length=300, blank=True, null=True)

    # Персональные данные
    first_name = models.CharField(verbose_name='Ваше имя', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Ваше фамилия', max_length=255, blank=True, null=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][1])
    address = models.CharField(verbose_name='Адрес', max_length=255, blank=True, null=True)
    phone = PhoneField(verbose_name="Телефон", blank=True, help_text='Контакт телефона')
    city = models.CharField(verbose_name='Город', max_length=255, choices=CityType.choices, default=CityType.ALMATY)
    reserve_email = models.EmailField(verbose_name='Резервный email', max_length=255, blank=True, null=True)
    website = models.CharField(verbose_name='Веб сайт', max_length=255, blank=True, null=True)

    # Статусы
    branding = models.BooleanField(verbose_name='Брендинг', default=False)
    for_clients = models.BooleanField(verbose_name='Вы открываете это для клиента?', default=False)

    def __str__(self):
        return self.brand.brandname

    class Meta:
        verbose_name = 'Панель управление'
        verbose_name_plural = 'Панели управление'
