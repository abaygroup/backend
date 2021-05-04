from rest_framework.generics import views
from rest_framework import status, permissions, response
from rest_framework.response import Response
from .models import Brand
from .serializers import UserCreateSerializer

class Users(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        brands = Brand.objects.all()
        serializer = UserCreateSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    