from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    path('activities/', views.ActivityView.as_view()),
    path('products/', views.ProductsView.as_view())
]