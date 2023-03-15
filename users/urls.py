from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('users/', views.UserRegister.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)




# from rest_framework import routers
# from .views import UserViewSet
# from django.urls import path

# router = routers.DefaultRouter()
# router.register('api/users', UserViewSet, 'users')

# urlpatterns = router.urls