from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Membership, Profile

User = get_user_model()


# User serializer
class UserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =('id', 'username', 'email', 'full_name', 'phone', 'gender', 'birthday',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("full_name", )


class UserChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# =============================================================


# Membership serializer
class MembershipSerializer(serializers.ModelSerializer):
    membership_type = serializers.CharField(source='get_membership_type_display')

    class Meta:
        model = Membership
        fields = ('slug', 'membership_type', 'price',)


# Profile
# ================================================================================
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'branding',)

# ================================================================================