from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response

from accounts.models import Brand
from products.models import Product, SuperCategory, SubCategory, Videohosting
from dashboard.models import Category
from .serializers import ( MediahostingMainProductListSerializer, MediahostingProductSerializer,
                           SubCategorySerializer, SupCategorySerializer,
                           ProfileSerializer, VideoHostingListSerializer, VideoHostingSerializer)


# Main Page View
class MainAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request):
        future_products = Product.objects.filter(production=False)[:4]
        last_products = Product.objects.filter(production=True)[:8]
        last_products_serializer = MediahostingMainProductListSerializer(last_products, many=True, context={"request": request})
        future_products_serializer = MediahostingMainProductListSerializer(future_products, many=True, context={"request": request})

        context = {
            "last_products": last_products_serializer.data,
            "future_products": future_products_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)



class SearchView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request):
        sup_categories = SuperCategory.objects.all()
        sub_categories = SubCategory.objects.all()
        sup_categories_serializer = SupCategorySerializer(sup_categories, many=True)
        sub_categories_serializer = SubCategorySerializer(sub_categories, many=True, context={"request": request})

        context = {
            "sup_categories": sup_categories_serializer.data,
            "sub_categories": sub_categories_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)



# Search Page View
class CategoryDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request, slug):
        sub_category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(subcategory=sub_category, production=True)
        sub_category_serializer = SubCategorySerializer(sub_category, context={"request": request})
        products_serializer = MediahostingMainProductListSerializer(products, many=True, context={"request": request})

        context = {
            "sub_category": sub_category_serializer.data,
            "products": products_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)



# Profile Page View
class ProfileView(views.APIView):

    def get(self, request, brandname):
        brand = get_object_or_404(Brand, brandname=brandname)
        profile = ProfileSerializer(brand.dashboard, partial=True, context={"request": request})
        products = MediahostingMainProductListSerializer(brand.product_set.filter(production=True), many=True, context={"request": request})

        context = {
            "profile": profile.data,
            "products": products.data
        }
        return Response(context, status=status.HTTP_200_OK)



# Product Detail View
class ProductDetailView(views.APIView):

    def get(self, request, isbn_code):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        videohosting = product.videohosting_set.all()
        product = MediahostingProductSerializer(product, partial=True, context={"request": request})
        videohosting = VideoHostingListSerializer(videohosting, many=True)

        context = {
            "product": product.data,
            "videohosting": videohosting.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Videohosting View
class VideoHostingView(views.APIView):

    def get(self, request, isbn_code, id):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        videohosting = product.videohosting_set.filter(access=True)
        video = get_object_or_404(Videohosting, id=id)
        video.view += 1
        video.save()
        video = VideoHostingSerializer(video, partial=True)
        videohosting = VideoHostingListSerializer(videohosting, many=True)

        context = {
            "video": video.data,
            "videohosting": videohosting.data
        }

        return Response(context, status=status.HTTP_200_OK)
