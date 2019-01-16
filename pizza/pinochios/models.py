from django.db import models

# Create your models here.
class Topping(models.Model):
    topping = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.topping}"

class Regular_Pizza(models.Model):
    name = models.CharField(max_length=20)
    small_price = models.FloatField(blank=True)
    large_price = models.FloatField(blank=True)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="Regular_Pizzas")
    number_of_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.small_price} for large, {self.large_price} for large" 

class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=20)
    small_price = models.FloatField(blank=True)
    large_price = models.FloatField(blank=True)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="Sicilian_Pizzas")
    number_of_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.small_price} for large, {self.large_price} for large"

class Sub(models.Model):
    name = models.CharField(max_length=20)
    small_price = models.FloatField(blank=True)
    large_price = models.FloatField(blank=True)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="Subs")
    built_in_topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.small_price} for large, {self.large_price} for large"
    
class Pasta(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} for {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} for {self.price}"

class Dinner_Platter(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} for {self.price}"


class Shopping_Cart_Item(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=20)
    type_of = models.CharField(max_length=20)
    price = models.FloatField(blank=True, null=True)
    small_price = models.FloatField(blank=True, null=True)
    large_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} | {self.type_of} - {self.name} single price is {self.price}, else {self.small_price} for small, {self.large_price} for large for user {self.user_id}"



