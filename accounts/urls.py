from django.urls import path
from .views import Users, ChangePasswordView

urlpatterns = [
    path('users/', Users.as_view()),
    path('password-change/', ChangePasswordView.as_view())
]