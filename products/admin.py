from django.contrib import admin
from .models import Activity, Product, Features, Videohosting, Comment


# Xарактеристики продукта
class FeaturesTable(admin.TabularInline):
    model = Features
    fields = ('product', 'label', 'value')
    extra = 0

# ===============================================


# Admin продукта
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'first_price', 'last_price', 'timestamp', 'last_update')
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'brand', 'owner', 'category', 'subcategory', 'picture', 'about', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Доступ', {'fields': ('observers',)}),
        ('Продакшен', {'fields': ('production',)})
    )
    list_filter = ('production',)
    search_fields = ('title', 'about', 'body', 'category',)
    ordering = ('-timestamp',)
    inlines = [ FeaturesTable, ]
    filter_horizontal = ()
# ===============================================



# Admin видеохостинга
class CommentTable(admin.TabularInline):
    model = Comment
    fields = ('owner', 'body',)
    extra = 0

class VidehostingAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'timestamp',)
    fieldsets = (
        ('Описание', {'fields': ('title', 'product', 'body', 'frame_url', 'access',)}),
    )
    list_filter = ('access',)
    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    inlines = [CommentTable, ]
    filter_horizontal = ()
# ===============================================


admin.site.register(Product, ProductAdmin)
admin.site.register(Videohosting, VidehostingAdmin)

admin.site.register(Activity)
admin.site.register(Features)
