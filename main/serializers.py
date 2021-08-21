from rest_framework import serializers
from .models import Post
from products.models import Product, SuperCategory, SubCategory
from accounts.serializers import UserCreateSerializer


# Product
# ==========================================================================
class MediahostingMainProductListSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'body', 'production', 'owner',)

# ==========================================================================


# Category
# ==========================================================================
class SupCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

# ==========================================================================


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date_created',)