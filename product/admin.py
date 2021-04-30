from django.contrib import admin
from .models import Notebook, Fridge

# NotebookAdmin
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'first_price', 'last_price',)
    # list_filter = ('is_physical',)
    fieldsets = (
        ('Описание продукта', {'fields': ('title', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Основные характеристики', {'fields': ('laptop_class', 'series', )}),
        ('Процессор', {'fields': ('processor_clock_speed', 'processor_series', )}),
    )

    # inlines = (Additionalimageinline,)
    search_fields = ('title', 'body', 'category',)
    ordering = ('-timestamp',)
    filter_horizontal = ()

# FridgeAdmin
class FridgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'first_price', 'last_price',)
    # list_filter = ('is_physical',)
    fieldsets = (
        ('Описание продукта', {'fields': ('title', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Основные характеристики', {'fields': ('useful_total_volume', 'open_door_signal', )}),
        ('Морозильная камера', {'fields': ('freezer_defrost_system', 'number_of_sections', )}),
    )

    # inlines = (Additionalimageinline,)
    search_fields = ('title', 'body', 'category',)
    ordering = ('-timestamp',)
    filter_horizontal = ()


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Fridge, FridgeAdmin)