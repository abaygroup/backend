from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions, response
from rest_framework.response import Response

from .models import Dashboard, Activity, Product, OverviewProducts
from .serializers import DashboardSerializer, ActivitySerializer

from django.utils import timezone
from django.core import serializers


# Главная страница панель управления
# ============================================
class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)

        # Проверка срок активности (Не больше 1 месяц)
        activities = Activity.objects.filter(owner=request.user).order_by('-created_at')[:5]
        for activity in activities:
            if activity.expiration_date < timezone.now():
                activity.delete()
        
        # Продукты
        overview_products = OverviewProducts.objects.get_overview_products('shoes', 'backpacks', request=request.user)
        products = sorted(overview_products, key=lambda instance: instance.timestamp, reverse=True)[:3]

        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})
        products = serializers.serialize('json', products, fields=["title", "isbn_code", "timestamp"])
       
        context = {
            'dashboard': dashboard_serializer.data,
            'activities': activities_serializer.data,
            'products': products
        }
        return Response(context, status=status.HTTP_200_OK)


# Список активности
# ==================================
class ActivityView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        # Проверка срок активности (Не больше 1 месяц)
        activities = Activity.objects.filter(owner=request.user).order_by('-created_at')
        for activity in activities:
            if activity.expiration_date < timezone.now():
                activity.delete()
        
        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})
        context = {
            'dashboard': dashboard_serializer.data,
            'activities': activities_serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)


class ProductsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request): 
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        overview_products = OverviewProducts.objects.get_overview_products('shoes', 'backpacks', request=request.user)
        
        products = sorted(overview_products, key=lambda instance: instance.timestamp, reverse=True)
        products = serializers.serialize('json', products)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})

        context = {
            'dashboard': dashboard_serializer.data,
            'products': products,
        }
        return Response(context, status=status.HTTP_200_OK)