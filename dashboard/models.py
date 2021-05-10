from django.db import models
from accounts.models import Brand
from django.core.exceptions import ValidationError
from phone_field import PhoneField
import uuid
import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType


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
        CLOTHES = 'CLOTHES', 'Одежда'
        VIRTUAL_SERVICES = 'VIRTUAL_SERVICES', 'Виртуальные сервисы'

        BEAUTY = 'BEAUTY', 'Красота'
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
        ANOTHER = 'ANOTHER', 'Другой'
        NOT_SELECTED = 'NOT_SELECTED', 'Не выбран' 

    GENDER_CHOICES = (
        ('N', 'Не указано'),
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    def validate_logotype(logotype):
        filesize = logotype.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла должно быть %sMB" % str(megabyte_limit))

    # Направление бренда или магазина
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    logotype = models.ImageField(verbose_name='Логотип', validators=[validate_logotype], upload_to='dashboard/avatar/', blank=True, null=True, help_text='Максимальный размер файла 2MB')
    branch = models.CharField(verbose_name='Отрасль', max_length=50, choices=Branch.choices, default=Branch.NOT_SELECTED)
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



# Категория
class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категорий', max_length=255)
    slug = models.SlugField(verbose_name='Ключовой адрес', max_length=255, unique=True)
    image = models.ImageField(verbose_name='Изброжение', upload_to='dashboard/categories/', blank=True, null=True)

    def __str__(self):
        return self.category_name    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'




# Недавняя активность
class Activity(models.Model):
    message = models.CharField(verbose_name="Сообщение", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


# Абстрактный модель Product
class Product(models.Model):
    # Описание
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Владелец')
    title = models.CharField(verbose_name='Заголовка', max_length=255)
    body = models.TextField(verbose_name='Описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='Изброжения', upload_to='dashboard/products/', blank=True, null=True)
    # Цены 
    first_price = models.DecimalField(verbose_name='От', max_digits=8, decimal_places=2)
    last_price = models.DecimalField(verbose_name='До', max_digits=8, decimal_places=2)
    # Код товара
    isbn_code = models.UUIDField(verbose_name='Коды товара(ISBN, UPC, GTIN)', unique=True, default=uuid.uuid4, editable=False)
    # Время 
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)
    # Просмотры
    view = models.IntegerField(verbose_name='Просмотров', default=0)
    

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        instance = self.title
        activity = Activity.objects.create(message="Вы импортировали продукт {}".format(instance), expiration_date=timezone.now() + datetime.timedelta(hours=1))
        activity.save()
        super(Product, self).save(*args, **kwargs)

    

    class Meta:
        abstract = True
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-timestamp',)



class OverviewProductsManager:
    
    @staticmethod
    def get_overview_products(*args, **kwargs):
        request = kwargs['request']
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.filter(owner=request)
            products.extend(model_products)

        return products


class OverviewProducts:

    objects = OverviewProductsManager()

