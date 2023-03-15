from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('api/v1/signup/', views.UserSignUp.as_view()),
    path('api/v1/profile/<int:pk>/', views.UserEditProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)