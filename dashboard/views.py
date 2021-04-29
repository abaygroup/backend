from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions, response
from rest_framework.response import Response

from .models import Dashboard
from .serializers import DashboardSerializer

class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

    def get(self, request):
        dashboard = get_object_or_404(Dashboard, brand=request.user)
        dashboard_serializer = DashboardSerializer(dashboard, context={"request": request})
        return Response(dashboard_serializer.data, status=status.HTTP_200_OK)