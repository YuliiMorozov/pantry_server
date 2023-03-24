from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=16)
    cost = models.PositiveIntegerField(default=0)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ingredient is {self.name}, cost {self.cost}"

class Cake(models.Model):
    name = models.CharField(max_length=16)
    # composition = models.TextField(blank=True)
    recipe = models.TextField(blank=True)
    prime_cost = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return f"Cake is {self.name}, prime cost is {self.prime_cost}, selling price is {self.selling_price}"
    
class Ingredient_Cake(models.Model):
    name = models.CharField(max_length=16)
    cost = models.PositiveIntegerField(default=0)

    cake_id = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ingredient is {self.name}, cost {self.cost}"