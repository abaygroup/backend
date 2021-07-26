from rest_framework import serializers
from .models import Dashboard, Notification
from accounts.serializers import UserCreateSerializer
from products.serializers import CategorySerializer

# Serializer для панель управления
# ==========================================================

class DashboardOverviewSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer()

    class Meta:
        model = Dashboard
        fields = ("id", "brand", "branch", "logotype", "website", "branding")



class DashboardSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer(read_only=True)
    gender = serializers.CharField(source='get_gender_display')
    branch = CategorySerializer(read_only=True)
    city = serializers.CharField(source='get_city_display')

    class Meta:
        model = Dashboard
        fields = '__all__'


class DashboardFormSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer(read_only=True)
    branch = CategorySerializer(read_only=True)

    class Meta:
        model = Dashboard
        fields = '__all__'

# ==========================================================


# Serializer для Уведомление
# ==========================================================
class NotificationSerializer(serializers.ModelSerializer):
    to_send = UserCreateSerializer(read_only=True)
    from_send = UserCreateSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'

class NotificationFormSerializer(serializers.ModelSerializer):
    to_send = UserCreateSerializer(read_only=True)
    from_send = UserCreateSerializer(read_only=True)

    class Meta:
        model = Notification
        exclude = ('checked',)