from django.db import models
from dashboard.models import Product, Category

# Электроника
# ====================================
class Electronics(Product):
    category = models.ForeignKey(Category, verbose_name='Категория',  on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return "Электроника"

    class Meta:
        abstract = True
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроники'


# Ноутбуки
class Notebook(Electronics):
    # Основные характеристики
    laptop_class = models.CharField(verbose_name="Класс ноутбука", max_length=64, blank=True, null=True)
    series = models.CharField(verbose_name="Серия", max_length=64, blank=True, null=True)

    # Процессор
    processor_clock_speed = models.DecimalField(verbose_name="Тактовая частота процессора Turbo Boost, ГГц", max_digits=3, decimal_places=2)
    processor_series = models.CharField(verbose_name="Серия процессора", max_length=64)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'


# Холодильники 
class Fridge(Electronics):
    # Основные характеристики
    useful_total_volume = models.PositiveIntegerField(verbose_name="Полезный общий объем, л", blank=True, null=True)
    open_door_signal = models.BooleanField(verbose_name="Сигнал открытой двери", default=False)

    # Морозильная камера
    freezer_defrost_system = models.CharField(verbose_name="Система размораживания морозильной камеры", max_length=64, blank=True, null=True)
    number_of_sections = models.PositiveIntegerField(verbose_name="Количество секций", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'

# ============================================================
    