from django.db import models
from accounts.models import Brand
from products.models import Product

class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Автор')
    date_created = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_created']



class Favorite(models.Model):
    user = models.ForeignKey(Brand , related_name='favorites', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.user, self.product)

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'