from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, Membership, UserMembership, Subscription
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


# User Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal information'), {'fields': ('full_name', 'gender', 'birthday', 'phone', 'last_login',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'full_name', )
    ordering = ('username',)
    filter_horizontal = ()


# Profile admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    list_filter = ('branding',)
    fieldsets = (
        (_('User direction'), {'fields': ('user', 'image',)}),
        (_('Branding'), {'fields': ('branding',)}),
        (_('Personal information'), {'fields': ('about_me', 'address',)}),
    )

    search_fields = ('user',)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_type', 'slug', 'price', )
    list_filter = ('membership_type',)
    search_fields = ('membership_type', 'slug', 'price',)


class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership',)
    list_filter = ('membership',)
    search_fields = ('user', 'membership',)


admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(Subscription)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(Group)