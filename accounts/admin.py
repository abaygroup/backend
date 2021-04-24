from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Brand
from django.contrib.auth.models import Group

class BrandAdmin(BaseUserAdmin):
    list_display = ('brandname', 'email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('brandname', 'email', 'password')}),
        ('Личная информация', {'fields': ('last_login',)}),
        ('Разрешения', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('brandname', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('brandname', 'email',)
    ordering = ('brandname',)
    filter_horizontal = ()

admin.site.register(Brand, BrandAdmin)
admin.site.unregister(Group)
