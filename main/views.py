from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response

from accounts.models import Brand
from products.models import Product, SuperCategory, SubCategory, Videohosting
from dashboard.models import Category
from .serializers import ( MediahostingMainProductListSerializer, MediahostingProductSerializer,
                           SubCategorySerializer, SupCategorySerializer, FavoritesSerializer, FollowingSerializer,
                           ProfileSerializer, VideoHostingListSerializer, VideoHostingSerializer)


# Main Page View
class MainAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request):
        future_products = Product.objects.filter(production=False)[:4]
        last_products = Product.objects.filter(production=True)[:8]
        last_products_serializer = MediahostingMainProductListSerializer(last_products, many=True, context={"request": request})
        future_products_serializer = MediahostingMainProductListSerializer(future_products, many=True, context={"request": request})
        if request.user.is_authenticated:
            my_mediahosting = request.user.product_set.filter(production=True)[:8]
            favorites_products = request.user.favorites.all()[:8]
            following_products = request.user.observers.all()[:8]

            my_mediahosting = MediahostingMainProductListSerializer(my_mediahosting, many=True, context={"request": request})
            favorites_products = FavoritesSerializer(favorites_products, many=True, context={"request": request})
            following_products = FollowingSerializer(following_products, many=True, context={"request": request})

            context = {
                "future_products": future_products_serializer.data,
                "favorites_products": favorites_products.data,
                "following_products": following_products.data,
                "my_mediahosting": my_mediahosting.data,
                "last_products": last_products_serializer.data
            }
        else:
            context = {
                "future_products": future_products_serializer.data,
                "last_products": last_products_serializer.data
            }

        return Response(context, status=status.HTTP_200_OK)



# Search Page View
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



class CategoryDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request, slug):
        sub_category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(subcategory=sub_category, production=True)
        sub_category_serializer = SubCategorySerializer(sub_category, context={"request": request})
        products_serializer = MediahostingMainProductListSerializer(products, many=True, context={"request": request})
        if request.user.is_authenticated:
            favorites = FavoritesSerializer(request.user.favorites.all(), many=True)
            context = {
                "sub_category": sub_category_serializer.data,
                "products": products_serializer.data,
                "favorites": favorites.data
            }
        else:
            context = {
                "sub_category": sub_category_serializer.data,
                "products": products_serializer.data,
            }

        return Response(context, status=status.HTTP_200_OK)


# Following View
class FollowingView(views.APIView):

    def get(self, request):
        following_products = request.user.observers.all()
        following_products = FollowingSerializer(following_products, many=True, context={"request": request})

        return Response(following_products.data, status=status.HTTP_200_OK)


# MyMediahostingView View
class MyMediahostingView(views.APIView):

    def get(self, request):
        my_mediahosting = request.user.product_set.filter(production=True)
        my_mediahosting = MediahostingMainProductListSerializer(my_mediahosting, many=True, context={"request": request})

        return Response(my_mediahosting.data, status=status.HTTP_200_OK)


# Favorites View
class FavoritesView(views.APIView):

    def get(self, request):
        favorites_products = request.user.favorites.all()
        favorites_products = FavoritesSerializer(favorites_products, many=True, context={"request": request})

        return Response(favorites_products.data, status=status.HTTP_200_OK)


class AddToFavorite(views.APIView):

    def post(self, request, isbn_code):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        if product.favorites.filter(id=request.user.id).exists():
            product.favorites.remove(request.user)
            return Response({"message": "{} deleted".format(product.title)}, status=status.HTTP_204_NO_CONTENT)
        else:
            product.favorites.add(request.user)
            return Response({"message": "{} added".format(product.title)}, status=status.HTTP_201_CREATED)


# Profile Page View
class ProfileView(views.APIView):

    def get(self, request, brandname):
        brand = get_object_or_404(Brand, brandname=brandname)
        profile = ProfileSerializer(brand.dashboard, partial=True, context={"request": request})
        products = MediahostingMainProductListSerializer(brand.product_set.filter(production=True), many=True, context={"request": request})
        favorites = FavoritesSerializer(request.user.favorites.all(), many=True)

        context = {
            "profile": profile.data,
            "production_count": brand.product_set.filter(production=True).count(),
            "products": products.data,
            "favorites": favorites.data,
        }
        return Response(context, status=status.HTTP_200_OK)



# Product Detail View
class ProductDetailView(views.APIView):

    def get(self, request, isbn_code):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        videohosting = product.videohosting_set.all()
        product_serializer = MediahostingProductSerializer(product, partial=True, context={"request": request})
        videohosting = VideoHostingListSerializer(videohosting, many=True)
        favorites = FavoritesSerializer(request.user.favorites.all(), many=True)

        context = {
            "product": product_serializer.data,
            "videohosting": videohosting.data,
            "favorites": favorites.data,
            "published_count": product.videohosting_set.filter(access=True).count(),
            "private_count": product.videohosting_set.filter(access=False).count()
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
