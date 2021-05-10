from rest_framework import serializers
from .models import Dashboard, Category, Activity, OverviewProducts
from accounts.serializers import UserCreateSerializer


# Admin store serializers
# ==========================================================
# View serializer
class DashboardSerializer(serializers.ModelSerializer):
    brand = UserCreateSerializer()
    gender = serializers.CharField(source='get_gender_display')
    branch = serializers.CharField(source='get_branch_display')
    city = serializers.CharField(source='get_city_display')

    class Meta:
        model = Dashboard
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('message', 'created_at', )