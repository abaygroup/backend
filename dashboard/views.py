from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response

from .models import Dashboard
from .serializers import DashboardSerializer

class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        dashboard_serializer = DashboardSerializer(dashboard, partial=True)
        return Response(dashboard_serializer.data, status=status.HTTP_200_OK)