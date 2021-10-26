from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPIView.as_view()),
    path('categories/', views.SearchView.as_view()),
    path('category/<slug>/', views.CategoryDetailView.as_view()),
    path('following/', views.FollowingView.as_view()),
    path('mymediahosting/', views.MyMediahostingView.as_view()),
    path('favorites/', views.FavoritesView.as_view()),
    path('favorites/<isbn_code>/', views.AddToFavorite.as_view()),
    path('follow/<isbn_code>/', views.FollowView.as_view()),
    path('profile/<username>/', views.ProfileView.as_view()),
    path('product/<isbn_code>/', views.ProductDetailView.as_view()),
    # path('product/<isbn_code>/videohosting/<id>/', views.VideoHostingView.as_view())
]
