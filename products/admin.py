from django.contrib import admin
from .models import Activity, Product, Chapter, Features, Videohosting


# Xарактеристики продукта
class FeaturesTable(admin.TabularInline):
    model = Features
    fields = ('product', 'category', 'label', 'value')
    extra = 0


# ===============================================

class ChapterTable(admin.TabularInline):
    model = Chapter
    fields = ('product', 'name',)
    extra = 0


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
    inlines = [ChapterTable, FeaturesTable,]
    filter_horizontal = ()
# ===============================================


# Admin видеохостинга

class VidehostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'chapter', 'timestamp',)
    fieldsets = (
        ('Описание', {'fields': ('title', 'product', 'chapter', 'body', 'frame_url', 'access',)}),
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
