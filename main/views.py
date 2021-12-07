from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response

from accounts.models import User
from products.models import Product, SuperCategory, SubCategory, Videohosting
from profile.models import Category, Profile
from .serializers import ( MediahostingMainProductListSerializer, MediahostingProductSerializer,
                           SubCategorySerializer, SupCategorySerializer, FavoritesSerializer, FollowingSerializer,
                           ProfileSerializer, VideoHostingListSerializer, VideoHostingSerializer, FeatureSerializer,
                          )
from accounts.serializers import UserUpdateSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# Main Page View
class MainAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request):
        future_products = Product.objects.filter(production=False)[:4]
        last_products = Product.objects.filter(production=True)[:8]
        authors = Profile.objects.all()[:5]

        last_products_serializer = MediahostingMainProductListSerializer(last_products, many=True, context={"request": request})
        future_products_serializer = MediahostingMainProductListSerializer(future_products, many=True, context={"request": request})
        authors_serializer = ProfileSerializer(authors, many=True, context={"request": request})

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
                "last_products": last_products_serializer.data,
                "authors": authors_serializer.data
            }
        else:
            context = {
                "future_products": future_products_serializer.data,
                "last_products": last_products_serializer.data,
                "authors": authors_serializer.data
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
            return Response({"message": "{} deleted".format(product.title)}, status=status.HTTP_200_OK)
        else:
            product.favorites.add(request.user)
            return Response({"message": "{} added".format(product.title)}, status=status.HTTP_200_OK)


class FollowView(views.APIView):

    def post(self, request, isbn_code):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        if product.observers.filter(id=request.user.id).exists():
            product.observers.remove(request.user)
            return Response({"message": "You unfollow {}".format(product.title)}, status=status.HTTP_200_OK)
        else:
            product.observers.add(request.user)
            return Response({"message": "You follow {}".format(product.title)}, status=status.HTTP_200_OK)



# Profile Page View
class ProfileView(views.APIView):
    parser_classes = [MultiPartParser, FormParser, ]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = ProfileSerializer(user.profile, partial=True, context={"request": request})
        products = MediahostingMainProductListSerializer(user.product_set.filter(production=True), many=True, context={"request": request})
        favorites = FavoritesSerializer(request.user.favorites.all(), many=True, context={"request": request})

        context = {
            "profile": profile.data,
            "production_count": user.product_set.filter(production=True).count(),
            "products": products.data,
            "favorites": favorites.data,
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        user_serializer = UserUpdateSerializer(user, data=request.data)
        profile_serializer = ProfileSerializer(user.profile, data=request.data, partial=True, context={"request": request})
        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return Response({"success": "Profile edited successfully"})

        return Response({"error": "Error to profile edited!"}, status=status.HTTP_400_BAD_REQUEST)



# Product Detail View
class ProductDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, isbn_code):
        product = get_object_or_404(Product, isbn_code=isbn_code)
        videohosting = product.videohosting_set.all()
        features = product.features_set.all()
        product_serializer = MediahostingProductSerializer(product, partial=True, context={"request": request})
        videohosting_serializer = VideoHostingListSerializer(videohosting, many=True, context={"request": request})
        features = FeatureSerializer(features, many=True)

        if request.user.is_authenticated:
            favorites = FavoritesSerializer(request.user.favorites.all(), many=True)
            followings = FollowingSerializer(request.user.observers.all(), many=True)
            context = {
                "product": product_serializer.data,
                "videohosting": videohosting_serializer.data,
                "favorites": favorites.data,
                "followings": followings.data,
                "features": features.data,
                "published_count": videohosting.filter(access=True).count(),
                "private_count": videohosting.filter(access=False).count()
            }
        else:
            context = {
                "product": product_serializer.data,
                "videohosting": videohosting_serializer.data,
                "features": features.data,
                "published_count": videohosting.filter(access=True).count(),
                "private_count": videohosting.filter(access=False).count()
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
