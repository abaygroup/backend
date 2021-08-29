from rest_framework import serializers
from .models import Post
from products.models import Product, SuperCategory, SubCategory, Videohosting, Features
from dashboard.models import Dashboard
from accounts.serializers import UserCreateSerializer
from dashboard.serializers import SubCategorySerializer

# Product
# ==========================================================================
class MediahostingMainProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'about',)


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

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'about',)


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'about', )

# ================================================================================


# Profile
# ================================================================================
class ProfileSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer(read_only=True)

    class Meta:
        model = Dashboard
        fields = ('id', 'brand', 'first_name', 'last_name', 'logotype', 'branding',)


# ================================================================================


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date_created',)