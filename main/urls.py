from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPIView.as_view()),
    path('categories/', views.SearchView.as_view()),
    path('category/<slug>/', views.CategoryDetailView.as_view()),
    path('profile/<brandname>/', views.ProfileView.as_view()),
    path('product/<isbn_code>/', views.ProductDetailView.as_view()),
    path('product/<isbn_code>/videohosting/<id>/', views.VideoHostingView.as_view())
]
