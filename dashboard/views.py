from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Dashboard, Notification, SuperCategory
from products.models import Activity, Product
from accounts.models import Brand

from .serializers import DashboardSerializer, DashboardFormSerializer, DashboardOverviewSerializer, NotificationSerializer, NotificationFormSerializer
from products.serializers import ( ActivitySerializer, ProductOverviewSerializer )
from main.serializers import Post, PostSerializer

from django.utils import timezone


# Главная страница панель управления
# ============================================
class DashboardOverview(views.APIView):
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


class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})

        return Response(dashboard_serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        branch = request.user.dashboard.branch
        if not dashboard.branch:
            branch = get_object_or_404(SuperCategory, slug=request.data['branch'])
        dashboard_serializer = DashboardFormSerializer(dashboard, data=request.data)
        if dashboard_serializer.is_valid():
            dashboard_serializer.save(brand=request.user, branch=branch)
            return Response(dashboard_serializer.data)
        return Response(dashboard_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLogoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request):
        logotype = request.user.dashboard.logotype
        logotype.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)
# ==================================


# Список активности
# ==================================
class ActivityView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        admin = get_object_or_404(Brand, is_superuser=True)
        # Проверка срок активности (Не больше 1 месяц)
        activities = Activity.objects.filter(owner=request.user).order_by('-created_at')
        for activity in activities:
            if activity.expiration_date < timezone.now():
                activity.delete()
        
        # Сериализировать
        activities_serializer = ActivitySerializer(activities, many=True)
        dashboard_serializer = DashboardOverviewSerializer(dashboard, context={"request": request})
        post_serializer = PostSerializer(Post.objects.filter(owner=admin), many=True)
        context = {
            'dashboard': dashboard_serializer.data,
            'activities': activities_serializer.data,
            'posts': post_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

    def delete(self, request):
        activities = Activity.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================


# Список уведомление
# ==================================
class NotificationView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        notification = request.user.notification_set.all()
        serializer = NotificationSerializer(notification, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        admin = get_object_or_404(Brand, is_superuser=True)
        brand = request.user
        n_serializer = NotificationFormSerializer(data=request.data)
        if n_serializer.is_valid():
            n_serializer.save(from_send=admin, to_send=brand)
            return Response(n_serializer.data)


class NotificationCountView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        notification = request.user.notification_set.filter(checked=False).count()
        return Response({'nochecked_count': notification})



class AccessMessageView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, id):
        notification = get_object_or_404(Notification, id=id)

        notification.checked = True
        notification.save()
        return Response({'checked': notification.checked}, status=status.HTTP_201_CREATED)

# ==================================
