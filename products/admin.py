from django.contrib import admin
from .models import Category, Activity, Product, Features, AdditionalImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', )
    search_fields = ('category_name',)
    fieldsets = (
        ('Описание категорий', {'fields': ('category_name', 'slug',)}),
    )

    ordering = ('category_name',)
    filter_horizontal = ()


# Xарактеристики продукта
class FeaturesTable(admin.TabularInline):
    model = Features
    fields = ('product', 'label', 'value')
    extra = 0

class AdditionalImageTable(admin.TabularInline):
    model = AdditionalImage
    fields = ('image',)
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'first_price', 'last_price', 'timestamp',)
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'brand', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Продакшен', {'fields': ('production',)})
    )
    list_filter = ('production',)
    search_fields = ('title', 'body', 'category',)
    ordering = ('-timestamp',)
    inlines = [ FeaturesTable, AdditionalImageTable ]
    filter_horizontal = ()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Activity)
admin.site.register(Features)