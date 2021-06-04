from rest_framework import serializers
from accounts.serializers import UserCreateSerializer
from .models import Category, Activity, Product, Features, AdditionalImage


# Serializer для Категорий
# ========================================================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# ========================================================


# Serializer для Продукт
# ========================================================
class ProductOverviewSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)

    class Meta:
        model = Product
        fields= ("title", "owner", "isbn_code", "timestamp",)


class ProductListSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)

    class Meta:
        model = Product
        fields= ("title", "owner", "picture", "body", "isbn_code", "production", "view", "timestamp",)


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields= '__all__'
# ========================================================


# Serializer для Характеристика и Дополнительный иллюстраций
# ========================================================
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'label', 'value')


class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalImage
        fields = ('id', 'image',)
# ========================================================


# Serializer для Активность
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('message', 'created_at', )