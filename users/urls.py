from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('signup/', views.UserSignUp.as_view()),    
    path('signin/', views.UserSignIn.as_view()),
    path('signout/', views.UserSignOut.as_view()),
    path('profile/<int:pk>/', views.UserEditProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)