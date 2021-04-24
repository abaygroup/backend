from django.contrib import admin
from .models import Dashboard

class DashboradAdmin(admin.ModelAdmin):
    list_display = ('brand', 'branch', 'first_name', 'last_name', 'city', 'website', 'for_clients')
    list_filter = ('for_clients',)
    fieldsets = (
        ('Направление бренда или магазина', {'fields': ('brand', 'logotype', 'branch',)}),
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'gender', 'city', 'phone', 'reserve_email', 'website')}),
        ('Статусы', {'fields': ('for_clients', 'branding',)}),
    )

    search_fields = ('brand', 'reserve_email',)
    ordering = ('brand',)
    filter_horizontal = ()


admin.site.register(Dashboard, DashboradAdmin)