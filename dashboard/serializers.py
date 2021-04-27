from rest_framework import serializers
from .models import Dashboard
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
