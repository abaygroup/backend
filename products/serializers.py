from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Activity, Product, Features, Videohosting, SuperCategory, SubCategory


# ========================================================
class SuperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = ('id', 'name', 'slug',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug', )
# ========================================================


# ========================================================
class ProductOverviewSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields= ("title", "owner", "isbn_code", "timestamp",)


class ProductListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields= ("title", "owner", "picture", "about", "isbn_code", "production", "timestamp", "last_update")


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    category = SuperCategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    observers = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields= '__all__'
# ========================================================


# ========================================================
class VideohostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'body', 'frame_url', 'view', 'access', 'timestamp',)


# ========================================================


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'label', 'value')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('message', 'created_at', )