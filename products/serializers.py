from rest_framework import serializers
from accounts.serializers import UserCreateSerializer
from .models import Category, Activity, Product, Features, AdditionalImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer()
    class Meta:
        model = Product
        fields= '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('label', 'value')


class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalImage
        fields = ('image',)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('message', 'created_at', )