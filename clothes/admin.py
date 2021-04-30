from django.contrib import admin
from .models import Sneakers, Backpacks


class SneakersAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'first_price', 'last_price', )
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Характеристики', {'fields': ('upper_material', 'internal_material', 'sole_material', 'season', 'sport_type', 'country_of_manufacture', 'zip_closure', 'article_number', )}),
    )

    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    filter_horizontal = ()

class BackpacksAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'first_price', 'last_price', )
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Характеристики', {'fields': ('upper_material', 'width', 'height', 'bottom_width', 'shoulder_strap', 'season', 'color', 'pattern', 'sport_type', 'country_of_manufacture', 'zip_closure', 'article_number',)}),
    )

    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    filter_horizontal = ()

admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(Backpacks, BackpacksAdmin)