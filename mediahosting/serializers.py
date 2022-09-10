from rest_framework import serializers
from products.models import Product, Videohosting, Features, Chapter, SuperCategory, SubCategory
from accounts.serializers import UserSerializer
from products.serializers import SubCategorySerializer


# Product
# ==========================================================================
class MediahostingMainProductListSerializer(serializers.ModelSerializer):
    authors = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'album', 'isbn_code', 'authors', 'observers', 'favorites',)


class MediahostingProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'subcategory', 'album', 'about', 'body', 'isbn_code', 'production', 'owner', 'timestamp', 'last_update',)


# Videohosting serializers
# ===============================================================
class VideoHostingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'chapter', 'title', 'timestamp', 'access',)


class VideoHostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'chapter', 'title', 'frame_url', 'body',)


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'name', 'timestamp',)


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
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

# ================================================================================


# Favorite and Following Serializer
# ================================================================================
class FollowingSerializer(serializers.ModelSerializer):
    authors = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'album', 'isbn_code', 'authors', 'observers', 'favorites',)


class FavoritesSerializer(serializers.ModelSerializer):
    authors = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'album', 'isbn_code', 'authors', 'observers', 'favorites',)

# ================================================================================
