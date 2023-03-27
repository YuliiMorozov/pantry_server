from rest_framework import serializers
from .models import Ingredient, Cake, Ingredient_Cake


class IngredientSerializer(serializers.ModelSerializer):
    # user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ingredient
        fields = '__all__'

class CakeSerializer(serializers.ModelSerializer):
    # user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cake
        fields = '__all__'

class Ingredient_CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_Cake
        fields = '__all__'