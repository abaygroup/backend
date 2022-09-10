from django.urls import path
from . import views


urlpatterns = [
    path('pricing/', views.PricingView.as_view()),
    path('pricing/success-payment/', views.success_payment, name='success_payment'),
    path('pricing/failure-payment/', views.failure_payment, name='failure_payment'),
    path('pricing/<slug>/', views.pricing_detail, name='pricing_detail'),
    path('user/<username>/', views.user_profile, name='user_profile'),
]