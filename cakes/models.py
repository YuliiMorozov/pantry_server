# from django.db import models
# from django.contrib.auth.models import User


# class Ingredient(models.Model):
#     name = models.CharField(max_length=16)
#     cost = models.ImageField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Ingredient is {self.name}, cost {self.cost}"

# class Cake(models.Model):
#     name = models.CharField(max_length=16)
#     prime_cost = models.ImageField()
#     selling_price = models.ImageField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"Cake is {self.name}, prime cost is {self.prime_cost}, selling price is {self.selling_price}"