from rest_framework import serializers
from .models import Dashboard
from accounts.serializers import UserCreateSerializer
from products.serializers import CategorySerializer

# Serializer для панель управления
# ==========================================================

class DashboardOverviewSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer()

    class Meta:
        model = Dashboard
        fields = ("id", "brand", "logotype", "website", "branding")


class DashboardSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer()
    gender = serializers.CharField(source='get_gender_display')
    branch = CategorySerializer()
    city = serializers.CharField(source='get_city_display')

    class Meta:
        model = Dashboard
        fields = '__all__'

# ==========================================================
