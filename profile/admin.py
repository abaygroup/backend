from django.contrib import admin
from .models import Profile, Notification, SuperCategory, SubCategory, Author


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'branding',)
    list_filter = ('branding',)
    fieldsets = (
        ('Направление бренда или пользователья', {'fields': ('user', 'avatar', 'category',)}),
        ('Персональные данные', {'fields': ('body', 'address',)}),
        ('Статусы', {'fields': ('branding',)}),
    )

    search_fields = ('user',)
    ordering = ('user',)
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


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Notification)
admin.site.register(Author)
admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(SubCategory)