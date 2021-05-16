from django.db import models
import uuid
import datetime
from django.utils import timezone
from accounts.models import Brand

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
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE)
    message = models.CharField(verbose_name="Сообщение", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


# Модель Product
class Product(models.Model):
    # Описание
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Владелец')
    title = models.CharField(verbose_name='Заголовка', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    body = models.TextField(verbose_name='Описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='Изброжения', upload_to='dashboard/products/', blank=True, null=True)
    # Цены
    first_price = models.DecimalField(verbose_name='От', max_digits=8, decimal_places=2)
    last_price = models.DecimalField(verbose_name='До', max_digits=8, decimal_places=2)
    # Код товара
    isbn_code = models.UUIDField(verbose_name='Коды товара(ISBN, UPC, GTIN)', unique=True, default=uuid.uuid4,
                                 editable=False)
    # Время
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)
    # Просмотры
    view = models.IntegerField(verbose_name='Просмотров', default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        instance = self.title
        activity = Activity.objects.create(owner=self.owner, message="Вы импортировали продукт {}".format(instance),
                                           expiration_date=timezone.now() + datetime.timedelta(weeks=4))
        activity.save()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-timestamp',)


class AdditionalImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    image = models.ImageField(verbose_name="Изброжения", upload_to="dashboard/products/ai/", null=True, blank=True)

    def __str__(self):
        return "Дополнительная иллюстрация для {}".format(self.product.title)

    class Meta:
        verbose_name = 'Дополнительная иллюстрация'
        verbose_name_plural = 'Дополнительный иллюстрации'


# Xарактеристика
class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="categories")
    label = models.CharField(verbose_name="Названия", max_length=255)
    value = models.CharField(verbose_name="Значение", max_length=255, null=True, blank=True)


    def __str__(self):
        return  "{}: {}".format(self.category.category_name, self.product.title)

    class Meta:
        verbose_name = "Xарактеристика"
        verbose_name_plural = "Xарактеристики"
