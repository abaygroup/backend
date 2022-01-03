from django.db import models
import uuid
import datetime
from django.utils import timezone
from profile.models import SuperCategory, SubCategory
from accounts.models import User
from ckeditor.fields import RichTextField


# Недавняя активность
# =============================================================================================================
class Activity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовка', max_length=40)
    brand = models.CharField(verbose_name="Бренд", max_length=32)
    category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory', verbose_name='Подкатегория')
    about = models.TextField(verbose_name='Кратко о продукте', max_length=300, blank=True, null=True)
    body = RichTextField(verbose_name='Описание', blank=True, null=True)
    album = models.ImageField(verbose_name='Альбом', upload_to='profile/products/', blank=True, null=True)

    # Код товара
    isbn_code = models.UUIDField(verbose_name='Коды товара(ISBN, UPC, GTIN)', unique=True, default=uuid.uuid4, editable=False)

    observers = models.ManyToManyField(User, verbose_name='Подписчики', related_name='observers', blank=True)
    favorites = models.ManyToManyField(User, verbose_name='Избранные', related_name='favorites', blank=True)
    authors = models.ManyToManyField(User, verbose_name='Авторы', related_name="authors")

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
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'
        ordering = ('-timestamp',)



# Xарактеристика
# =============================================================================================================
class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Релиз")
    category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, verbose_name="Категория", related_name="categories")
    label = models.CharField(verbose_name="Названия", max_length=64)
    value = models.CharField(verbose_name="Значение", max_length=64, null=True, blank=True)


    def __str__(self):
        return  "{}: {}".format(self.category.name, self.product)

    class Meta:
        verbose_name = "Xарактеристика"
        verbose_name_plural = "Xарактеристики"


# Раздел
# =========================================================================
class Chapter(models.Model):
    # album = models.ImageField(verbose_name='Альбом', upload_to='profile/chapters/', blank=True, null=True)
    name = models.CharField(verbose_name='Название', max_length=64)
    # about = models.TextField(verbose_name='Кратко о разделе', max_length=300, blank=True)
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Релиз')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['timestamp']


# Видеохостинг
# =========================================================================
class Videohosting(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64)
    body = RichTextField(verbose_name='Описание', blank=True, null=True)
    frame_url = models.CharField(verbose_name='Ссылка', max_length=255)
    access = models.BooleanField(verbose_name='Доступ к видео', default=True)
    timestamp = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Релиз')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Раздел')

    # Просмотры
    view = models.IntegerField(verbose_name='Просмотров', default=0)

    def __str__(self):
        return "{} | {}".format(self.chapter, self.title)

    class Meta:
        verbose_name = "Видеохостинг"
        verbose_name_plural = "Видеохостинг"
        ordering = ['timestamp']