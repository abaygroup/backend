from rest_framework import serializers
from .models import Post
from products.models import Product, SuperCategory, SubCategory, Videohosting
from dashboard.models import Dashboard
from accounts.serializers import UserCreateSerializer


# Product
# ==========================================================================
class MediahostingMainProductListSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'isbn_code', 'body', 'production', 'owner',)


class MediahostingProductSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(read_only=True)


    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'picture', 'body', 'isbn_code', 'production', 'owner', 'timestamp', 'last_update',)


class VideoHostingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'timestamp', 'access',)


class VideoHostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videohosting
        fields = ('id', 'title', 'frame_url', 'body',)
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

# Profile
# ==========================================================================
class ProfileSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer(read_only=True)

    class Meta:
        model = Dashboard
        fields = ('id', 'brand', 'logotype', 'first_name', 'last_name', 'branding',)


# ==========================================================================

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date_created',)