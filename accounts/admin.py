from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'profile_name', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Личная информация', {'fields': ('profile_name', 'gender', 'birthday', 'phone', 'last_login',)}),
        ('Разрешения', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'profile_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'profile_name', )
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
