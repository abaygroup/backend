from django.shortcuts import get_object_or_404
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from products.models import Product, SubCategory
from products.serializers import ( ProductListSerializer, ProductDetailSerializer,
                                   FeatureSerializer,
                                   VideohostingSerializer)

from django.db.models import Q

# Продукты
# ==================================================================
# Список продукты
class ProductsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request):
        products = Product.objects.filter(owner=request.user)
        if 'search' in request.GET or 'production' in request.GET:
            search = request.GET.get('search')
            q = Q(title__icontains=search) | Q(body__icontains=search)
            qs = products.filter(q)
            products_serializer = ProductListSerializer(qs, context={"request": request}, many=True)
        else:
            products_serializer = ProductListSerializer(products, context={"request": request}, many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.dashboard.branding == True:
            subcategory = get_object_or_404(SubCategory, slug=request.data['subcategory'])
            product_serializer = ProductDetailSerializer(data=request.data)
            if product_serializer.is_valid():
                product_serializer.save(owner=request.user, category=request.user.dashboard.branch, subcategory=subcategory)
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)

            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "An error occurred while importing"})


# Профиль продукта
class ProductDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        videohosting = product.videohosting_set.all()
        features = product.features_set.all()

        product_serializer = ProductDetailSerializer(product, context={"request": request}, partial=True)
        videohosting_serializer = VideohostingSerializer(videohosting, many=True)
        features_serializer = FeatureSerializer(features, many=True)

        context = {
            "product": product_serializer.data,
            "videohosting": videohosting_serializer.data,
            "features": features_serializer.data,
            "observers_count": product.observers.count()
        }

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        subcategory = get_object_or_404(SubCategory, slug=request.data['subcategory'])
        product_serializer = ProductDetailSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save(subcategory=subcategory)
            return Response(product_serializer.data)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeletePictureView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        product.picture.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)

# ========================================================================


# Видеохостинг
# ========================================================================
class VidehostingView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, owner, isbn_code):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        video_serializer = VideohostingSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save(product=product)
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)

        return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VidehostingDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        video = product.videohosting_set.get(pk=pk)
        comment = video.comment_set.all()
        video_serializer = VideohostingSerializer(video)
        context = {
            'product': {"owner": product.owner.brandname, "isbn_code": product.isbn_code},
            'video': video_serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)


    def put(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        video = product.videohosting_set.get(pk=pk)
        video_serializer = VideohostingSerializer(video, data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data)

        return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        video = product.videohosting_set.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ========================================================================


# Характеристики
# ========================================================================
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

    def put(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        feature = product.features_set.get(pk=pk)
        feature_serializer = FeatureSerializer(feature, data=request.data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return Response(feature_serializer.data)

        return Response(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, owner, isbn_code, pk):
        product = get_object_or_404(Product, owner=request.user, isbn_code=isbn_code)
        feature = product.features_set.get(pk=pk)
        feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ===========================================================================