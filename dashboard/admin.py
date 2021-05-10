from django.contrib import admin
from .models import Dashboard, Category, Activity


class DashboradAdmin(admin.ModelAdmin):
    list_display = ('brand', 'branch', 'first_name', 'last_name', 'city', 'website', 'for_clients', 'branding',)
    list_filter = ('for_clients',)
    fieldsets = (
        ('Направление бренда или магазина', {'fields': ('brand', 'logotype', 'branch',)}),
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'gender', 'city', 'phone', 'reserve_email', 'website')}),
        ('Статусы', {'fields': ('for_clients', 'branding',)}),
    )

    search_fields = ('brand', 'reserve_email',)
    ordering = ('brand',)
    filter_horizontal = ()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'image',)
    search_fields = ('category_name',)
    fieldsets = (
        ('Описание категорий', {'fields': ('category_name', 'slug', 'image',)}),
    )

    ordering = ('category_name',)
    filter_horizontal = ()



admin.site.register(Dashboard, DashboradAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Activity)