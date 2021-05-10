from django.contrib import admin
from django import forms
from .models import Shoes, Backpacks
from dashboard.models import Category

class ShoesFormChoiseField(forms.ModelChoiceField):
    pass

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'first_price', 'last_price', )
    fieldsets = (
        ('Описание товара', {'fields': ('title', 'owner', 'category', 'picture', 'body',)}),
        ('Цены', {'fields': ('first_price', 'last_price',)}),
        ('Характеристики', {'fields': ('upper_material', 'internal_material', 'sole_material', 'season', 'sport_type', 'country_of_manufacture', 'zip_closure', 'article_number', )}),
    )

    search_fields = ('title', 'body',)
    ordering = ('-timestamp',)
    filter_horizontal = ()

    def formfield_for_foreignkey(self, db_field, request):
        if db_field.name == 'category':
            return ShoesFormChoiseField(Category.objects.filter(slug="clothing"))
        
        return super().formfield_for_foreignkey(db_field, request)



class BackpacksFormChoiseField(forms.ModelChoiceField):
    pass

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

    def formfield_for_foreignkey(self, db_field, request):
        if db_field.name == 'category':
            return BackpacksFormChoiseField(Category.objects.filter(slug="clothing"))
        
        return super().formfield_for_foreignkey(db_field, request)


admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Backpacks, BackpacksAdmin)