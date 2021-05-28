from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Dashboard
from products.models import Activity, Product
from .serializers import DashboardSerializer, DashboardOverviewSerializer
from products.serializers import (
    ActivitySerializer,
    ProductListSerializer, ProductOverviewSerializer, ProductDetailSerializer,
    FeatureSerializer, AISerializer)

from django.utils import timezone


# Главная страница панель управления
# ============================================
class DashboardOverviewView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)

        # Проверка срок активности (Не больше 1 месяц)
        activities = Activity.objects.filter(owner=request.user).order_by('-created_at')[:5]
        for activity in activities:
            if activity.expiration_date < timezone.now():
                activity.delete()
        
        # Продукты
        products = Product.objects.filter(owner=request.user)[:3]

        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardOverviewSerializer(dashboard, context={"request": request})
        products = ProductOverviewSerializer(products, context={"request": request}, many=True)
       
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
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        # Проверка срок активности (Не больше 1 месяц)
        activities = Activity.objects.filter(owner=request.user).order_by('-created_at')
        for activity in activities:
            if activity.expiration_date < timezone.now():
                activity.delete()
        
        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardOverviewSerializer(dashboard, context={"request": request})
        context = {
            'dashboard': dashboard_serializer.data,
            'activities': activities_serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request):
        activities = Activity.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Продукты
# ==================================================================

# Список продукты
class ProductsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request): 
        products = Product.objects.filter(owner=request.user)
        products_serializer = ProductListSerializer(products, context={"request": request}, many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = ProductDetailSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save(owner=request.user, category=request.user.dashboard.branch)
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Профиль продукта
class ProductDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        features = product.features_set.all()
        additionalImage = product.additionalimage_set.all()
        product_serializer = ProductDetailSerializer(product, context={"request": request}, partial=True)
        features_serializer = FeatureSerializer(features, many=True)
        ai_serializer = AISerializer(additionalImage, context={"request": request}, many=True)

        context = {
            "products": product_serializer.data,
            "features": features_serializer.data,
            "ai": ai_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        product_serializer = ProductDetailSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Характеристики
class FeaturesView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        features_serializer = FeatureSerializer(data=request.data)
        if features_serializer.is_valid():
            features_serializer.save(product=product, category=request.user.dashboard.branch)
            return Response(features_serializer.data, status=status.HTTP_201_CREATED)

        return Response(features_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeatureDetailView(views.APIView):
    parser_classes = [MultiPartParser, FormParser, ]

    def put(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        feature = product.features_set.get(pk=pk)
        feature_serializer = FeatureSerializer(feature, data=request.data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return  Response(feature_serializer.data)

        return Response(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        feature = product.features_set.get(pk=pk)
        feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Дополнительный иллюстрации
class AIView(views.APIView):
    parser_classes = [MultiPartParser, FormParser, ]

    def post(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        ai_serializer = AISerializer(data=request.data)
        if ai_serializer.is_valid():
            ai_serializer.save(product=product)
            return Response(ai_serializer.data, status=status.HTTP_201_CREATED)

        return Response(ai_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AIDetailView(views.APIView):
    parser_classes = [MultiPartParser, FormParser, ]

    def put(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        ai = product.additionalimage_set.get(pk=pk)
        ai_serializer = AISerializer(ai, data=request.data)
        if ai_serializer.is_valid():
            ai_serializer.save()
            return  Response(ai_serializer.data)

        return Response(ai_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        ai = product.additionalimage_set.get(pk=pk)
        ai.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ===========================================================================