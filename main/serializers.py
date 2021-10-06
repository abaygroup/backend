from rest_framework import serializers
from .models import Post
from products.models import Product, SuperCategory, SubCategory, Videohosting, Features, Author
from dashboard.models import Dashboard
from accounts.serializers import UserCreateSerializer
from dashboard.serializers import SubCategorySerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "full_name", "picture", "about", )


# Product
# ==========================================================================
class MediahostingMainProductListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'authors',)


class MediahostingProductSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'subcategory', 'picture', 'about', 'body', 'isbn_code', 'production', 'owner', 'timestamp', 'last_update',)



class VideoHostingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'timestamp', 'access',)


class VideoHostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'frame_url', 'body',)



class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'label', 'value')
# ================================================================================


# Category
# ================================================================================
class SupCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

# ================================================================================

# Favorite and Following Serializer
# ================================================================================
class FollowingSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'authors',)


class FavoritesSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'authors', )

# ================================================================================


# Profile
# ================================================================================
class ProfileSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer(read_only=True)

    class Meta:
        model = Dashboard
        fields = ('id', 'brand', 'full_name', 'logotype', 'branding',)


# ================================================================================


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date_created',)