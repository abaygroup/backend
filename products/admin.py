from django.contrib import admin
from .models import Activity, Product, Features, Videohosting


# Xарактеристики продукта
class FeaturesTable(admin.TabularInline):
    model = Features
    fields = ('product', 'category', 'label', 'value')
    extra = 0


# ===============================================


# Admin продукта
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'timestamp', 'last_update')
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'brand', 'owner', 'category', 'subcategory', 'album', 'about', 'body',)}),
        ('Доступ', {'fields': ('favorites', 'observers', 'authors', )}),
        ('Продакшен', {'fields': ('production',)})
    )
    list_filter = ('production',)
    search_fields = ('title', 'about', 'body', 'category',)
    ordering = ('-timestamp',)
    inlines = [FeaturesTable,]
    filter_horizontal = ()
# ===============================================



# Admin видеохостинга

class VidehostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'timestamp',)
    fieldsets = (
        ('Описание', {'fields': ('title', 'product', 'body', 'frame_url', 'access',)}),
    )
    list_filter = ('access',)
    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    filter_horizontal = ()
# ===============================================


admin.site.register(Product, ProductAdmin)
admin.site.register(Videohosting, VidehostingAdmin)

admin.site.register(Activity)
admin.site.register(Features)
