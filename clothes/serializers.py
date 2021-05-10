from rest_framework import serializers
from .models import Shoes, Backpacks

class ShoesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shoes
        fields = '__all__'


class BackpacksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Backpacks
        fields = '__all__'