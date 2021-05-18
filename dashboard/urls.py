from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardOverviewView.as_view()),
    path('activities/', views.ActivityView.as_view()),
    path('products/', views.ProductsView.as_view()),
    path('product/<owner>/<isbn_code>/', views.ProductDetailView.as_view()),
    path('product/<owner>/<isbn_code>/features/', views.FeaturesView.as_view()),
    path('product/<owner>/<isbn_code>/feature/<int:pk>/', views.FeatureDetailView.as_view()),
    path('product/<owner>/<isbn_code>/ais/', views.AIView.as_view()),
    path('product/<owner>/<isbn_code>/ai/<int:pk>/', views.AIDetailView.as_view())
]