from django.db import models
from dashboard.models import Product, Category

# Одежда
# ====================================
class Clothes(Product):
    category = models.ForeignKey(Category, verbose_name='Категория',  on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return "Одежда"

    class Meta:
        abstract = True
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'


# Обувь
class Shoes(Clothes):
    upper_material = models.CharField(verbose_name="Материал верха", max_length=64, blank=True, null=True)
    internal_material = models.CharField(verbose_name="Внутренний материал", max_length=64, blank=True, null=True)
    sole_material = models.CharField(verbose_name="Материал подошвы", max_length=64, blank=True, null=True)
    season = models.CharField(verbose_name="Сезон", max_length=64, blank=True, null=True)
    color = models.CharField(verbose_name="Цвет", max_length=64, blank=True, null=True)
    sport_type = models.CharField(verbose_name="Вид спорта", max_length=64, blank=True, null=True)
    country_of_manufacture = models.CharField(verbose_name="Страна производства", max_length=64, blank=True, null=True)
    zip_closure = models.CharField(verbose_name="Застежка", max_length=64, blank=True, null=True)
    article_number = models.CharField(verbose_name="Артикул", max_length=64, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'

# ============================================================


# Рюкзаки и сумки
class Backpacks(Clothes):
    upper_material = models.CharField(verbose_name="Материал верха", max_length=64, blank=True, null=True)
    width = models.PositiveIntegerField(verbose_name="Ширина", blank=True, null=True)
    height = models.PositiveIntegerField(verbose_name="Высота", blank=True, null=True)
    bottom_width = models.PositiveIntegerField(verbose_name="Ширина дна", blank=True, null=True)
    shoulder_strap = models.PositiveIntegerField(verbose_name="Плечевой ремень", blank=True, null=True)
    season = models.CharField(verbose_name="Сезон", max_length=64, blank=True, null=True)
    color = models.CharField(verbose_name="Цвет", max_length=64, blank=True, null=True)
    pattern = models.CharField(verbose_name="Узор", max_length=64, blank=True, null=True)
    sport_type = models.CharField(verbose_name="Вид спорта", max_length=64, blank=True, null=True)
    country_of_manufacture = models.CharField(verbose_name="Страна производства", max_length=64, blank=True, null=True)
    zip_closure = models.CharField(verbose_name="Застежка", max_length=64, blank=True, null=True)
    article_number = models.CharField(verbose_name="Артикул", max_length=64, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Рюкзак и сумку"
        verbose_name_plural = "Рюкзаки и сумки"

# ============================================================
