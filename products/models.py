from django.db import models
import uuid
import datetime
from django.utils import timezone
from dashboard.models import SuperCategory, SubCategory
from accounts.models import Brand


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
# =========================================================================
class Product(models.Model):
    # Описание
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Владелец')
    title = models.CharField(verbose_name='Заголовка', max_length=40)
    brand = models.CharField(verbose_name="Бренд", max_length=32)
    category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory', verbose_name='Подкатегория')
    about = models.TextField(verbose_name='Кратко о продукте', max_length=300, blank=True, null=True)
    body = models.TextField(verbose_name='Описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='Изброжения', upload_to='dashboard/products/', blank=True, null=True)
    # Цены
    first_price = models.DecimalField(verbose_name='От', max_digits=9, decimal_places=2)
    last_price = models.DecimalField(verbose_name='До', max_digits=9, decimal_places=2)
    # Код товара
    isbn_code = models.UUIDField(verbose_name='Коды товара(ISBN, UPC, GTIN)', unique=True, default=uuid.uuid4, editable=False)
    observers = models.ManyToManyField(Brand, verbose_name='Студенты', related_name='observers', blank=True)

    favorites = models.ManyToManyField(Brand, verbose_name='Избранные', related_name='favorites', blank=True)

    # Время
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name='Последнее обновление', auto_now=True)

    # Продакшен
    production = models.BooleanField(verbose_name="Публикация", default=False)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        instance = self.title
        activity = Activity.objects.create(owner=self.owner, message="Вы импортировали продукт {}".format(instance),
                                           expiration_date=timezone.now() + datetime.timedelta(weeks=1))
        if self.title:
            activity.save()

        super(Product, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        instance = self.title
        activity = Activity.objects.create(owner=self.owner, message="Вы удалили продукт {}".format(instance),
                                           expiration_date=timezone.now() + datetime.timedelta(weeks=1))
        if self.title:
            activity.save()

        super(Product, self).delete(*args, **kwargs)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-timestamp',)



# Xарактеристика
class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, verbose_name="Категория", related_name="categories")
    label = models.CharField(verbose_name="Названия", max_length=64)
    value = models.CharField(verbose_name="Значение", max_length=64, null=True, blank=True)


    def __str__(self):
        return  "{}: {}".format(self.category.name, self.product)

    class Meta:
        verbose_name = "Xарактеристика"
        verbose_name_plural = "Xарактеристики"



# Видеохостинг
# =========================================================================
class Videohosting(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64)
    body = models.TextField(verbose_name='Описание', blank=True)
    frame_url = models.CharField(verbose_name='Ссылка', max_length=255)
    access = models.BooleanField(verbose_name='Доступ к видео', default=True)
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    # Просмотры
    view = models.IntegerField(verbose_name='Просмотров', default=0)

    def __str__(self):
        return "{} | {}".format(self.product, self.title)

    class Meta:
        verbose_name = "Видеохостинг"
        verbose_name_plural = "Видеохостинг"
        ordering = ['title']



class Comment(models.Model):
    videohosting = models.ForeignKey(Videohosting, on_delete=models.CASCADE, verbose_name='Видеохостинг')
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Автор')
    body = models.TextField(verbose_name='Тело комментарий', max_length=300)
    timestamp = models.DateTimeField(verbose_name='Дата написание', auto_now_add=True)

    def __str__(self):
        return "{}|{}".format(self.owner, self.videohosting)


    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


