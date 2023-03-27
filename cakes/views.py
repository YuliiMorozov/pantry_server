from django.contrib.auth.models import User

from .models import Ingredient
from .serializers import Ingredient_CakeSerializer, IngredientSerializer, CakeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class AddIngredient(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()    
    # serializer_class = IngredientSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return IngredientSerializer
        else:
            return Ingredient_CakeSerializer


class CreateCake(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()    
    serializer_class = CakeSerializer

#     def get_queryset(self, pk):
#         return User.objects.get(pk=pk)  