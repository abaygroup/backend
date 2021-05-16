from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response

from .models import Dashboard
from products.models import Activity, Product
from .serializers import DashboardSerializer
from products.serializers import ActivitySerializer, ProductSerializer, FeatureSerializer, AISerializer

from django.utils import timezone


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
        products = Product.objects.filter(owner=request.user)

        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})
        products = ProductSerializer(products, context={"request": request}, many=True)
       
        context = {
            'dashboard': dashboard_serializer.data,
            'activities': activities_serializer.data,
            'products': products.data
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



# Список товаров
# ==================================================================
class ProductsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request): 
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        products = Product.objects.filter(owner=request.user)
        
        products_serializer = ProductSerializer(products, context={"request": request}, many=True)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})

        context = {
            'dashboard': dashboard_serializer.data,
            'products': products_serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)


class ProductDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        features = product.features_set.all()
        additionalImage = product.additionalimage_set.all()
        product_serializer = ProductSerializer(product, context={"request": request}, partial=True)
        features_serializer = FeatureSerializer(features, many=True)
        ai_serializer = AISerializer(additionalImage, context={"request": request}, many=True)

        context = {
            "products": product_serializer.data,
            "features": features_serializer.data,
            "ai": ai_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)