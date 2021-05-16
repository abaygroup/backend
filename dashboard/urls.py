from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    path('activities/', views.ActivityView.as_view()),
    path('products/', views.ProductsView.as_view()),
    path('product/<owner>/<isbn_code>/', views.ProductDetailView.as_view())
]