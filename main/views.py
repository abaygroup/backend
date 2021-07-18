from rest_framework import views, status, permissions
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductListSerializer


class MainAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
