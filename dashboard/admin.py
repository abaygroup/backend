from django.contrib import admin
from .models import Dashboard, Notification, SuperCategory, SubCategory, Author


class DashboradAdmin(admin.ModelAdmin):
    list_display = ('brand', 'branch', 'full_name', 'website', 'for_clients', 'branding',)
    list_filter = ('for_clients',)
    fieldsets = (
        ('Направление бренда или пользователья', {'fields': ('brand', 'logotype', 'branch',)}),
        ('Персональные данные', {'fields': ('full_name', 'gender', 'phone', 'address', 'reserve_email', 'website')}),
        ('Статусы', {'fields': ('for_clients', 'branding',)}),
    )

    search_fields = ('brand', 'reserve_email',)
    ordering = ('brand',)
    filter_horizontal = ()


class SubCategoryInline(admin.TabularInline):
    model = SubCategory

class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    exclude = ('super_category',)
    fieldsets = (
        ('Описание категорий', {'fields': ('name', 'slug',)}),
    )
    inlines = (SubCategoryInline,)
    filter_horizontal = ()
# ===============================================


admin.site.register(Dashboard, DashboradAdmin)
admin.site.register(Notification)
admin.site.register(Author)
admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(SubCategory)