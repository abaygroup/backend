from rest_framework import serializers
from accounts.serializers import UserCreateSerializer
from .models import Activity, Product, Features, AdditionalImage, Videohosting, Comment, Docs
from dashboard.serializers import SuperCategorySerializer, SubCategorySerializer

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
        fields= ("title", "owner", "picture", "body", "isbn_code", "production", "timestamp", "last_update")


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)
    category = SuperCategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    observers = UserCreateSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields= '__all__'
# ========================================================


# Serializer для Характеристика и Дополнительный иллюстраций
# ========================================================
class VideohostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'body', 'frame_url', 'view', 'access', 'timestamp',)


class CommentSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)
    class Meta:
        model = Comment
        exclude = ('videohosting',)


class DocsSerializer(serializers.ModelSerializer):
    videohosting = VideohostingSerializer(read_only=True)
    class Meta:
        model = Docs
        fields = '__all__'



# Serializer для Характеристика и Дополнительный иллюстраций
# ===========================================================
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