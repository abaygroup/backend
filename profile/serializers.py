from rest_framework import serializers
from .models import Profile, Notification, SubCategory, SuperCategory
from accounts.serializers import UserCreateSerializer


# Serializer для Категорий
# ========================================================
class SuperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = ('id', 'name', 'slug',)

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug',)
# ========================================================
#
#
# # Serializer для панель управления
# # ==========================================================
# class ProfileOverviewSerializer(serializers.ModelSerializer):
#     user = UserCreateSerializer()
#     category = SuperCategorySerializer()
#
#     class Meta:
#         model = Profile
#         fields = ("id", "user", "category", "avatar", "branding",)
#
#
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserCreateSerializer(read_only=True)
#     category = SuperCategorySerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# class DashboardFormSerializer(serializers.ModelSerializer):
#     user = UserCreateSerializer(read_only=True)
#     category = SuperCategorySerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
# # ==========================================================
#
#
# # Serializer для Уведомление
# # ==========================================================
# class NotificationSerializer(serializers.ModelSerializer):
#     to_send = UserCreateSerializer(read_only=True)
#     from_send = UserCreateSerializer(read_only=True)
#
#     class Meta:
#         model = Notification
#         fields = '__all__'
#
# class NotificationFormSerializer(serializers.ModelSerializer):
#     to_send = UserCreateSerializer(read_only=True)
#     from_send = UserCreateSerializer(read_only=True)
#
#     class Meta:
#         model = Notification
#         exclude = ('checked',)
#
# # ==========================================================
