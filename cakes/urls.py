from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cakes import views

urlpatterns = [
    path('api/v1/ingredients/', views.AddIngredient.as_view()),
    path('api/v1/cakes/', views.CreateCake.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)