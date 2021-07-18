from django.contrib import admin
from .models import Category, Activity, Product, Features, AdditionalImage, Videohosting, Multilink


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
    list_display = ('title', 'owner', 'first_price', 'last_price', 'timestamp', 'last_update')
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'brand', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Доступ', {'fields': ('observers',)}),
        ('Продакшен', {'fields': ('production',)})
    )
    list_filter = ('production',)
    search_fields = ('title', 'body', 'category',)
    ordering = ('-timestamp',)
    inlines = [ FeaturesTable, AdditionalImageTable ]
    filter_horizontal = ()



class MultilinkTable(admin.TabularInline):
    model = Multilink
    fields = ('link',)
    extra = 0

class VidehostingAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'timestamp',)
    fieldsets = (
        ('Описание', {'fields': ('title', 'product', 'body', 'frame_url', 'access',)}),
    )
    list_filter = ('access',)
    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    inlines = [MultilinkTable]
    filter_horizontal = ()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Videohosting, VidehostingAdmin)
admin.site.register(Activity)
admin.site.register(Features)