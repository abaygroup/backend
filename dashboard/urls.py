from django.urls import path
from . import views as dashboard_view
from products import views as product_view

urlpatterns = [
    # Dashboard urls
    path('', dashboard_view.DashboardOverviewView.as_view()),
    path('owner/', dashboard_view.DashboardView.as_view()),
    path('activities/', dashboard_view.ActivityView.as_view()),
    path('notification/', dashboard_view.NotificationView.as_view()),

    # Product urls
    path('products/', product_view.ProductsView.as_view()),
    path('product/<owner>/<isbn_code>/', product_view.ProductDetailView.as_view()),
    path('product/<owner>/<isbn_code>/features/', product_view.FeaturesView.as_view()),
    path('product/<owner>/<isbn_code>/feature/<int:pk>/', product_view.FeatureDetailView.as_view()),
    path('product/<owner>/<isbn_code>/ais/', product_view.AIView.as_view()),
    path('product/<owner>/<isbn_code>/ai/<int:pk>/', product_view.AIDetailView.as_view()),

    # Videhosting
    path('product/<owner>/<isbn_code>/videohosting/', product_view.VidehostingView.as_view()),
    path('product/<owner>/<isbn_code>/video/<int:pk>/', product_view.VidehostingDetailView.as_view()),
    path('product/<owner>/<isbn_code>/video/<int:video_pk>/links/', product_view.MultiLinkView.as_view()),
    path('product/<owner>/<isbn_code>/video/<int:video_pk>/link/<int:pk>/', product_view.MultiLinkDetailView.as_view())

]