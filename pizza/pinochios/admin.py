from django.contrib import admin
from .models import Topping, Regular_Pizza, Sicilian_Pizza, Sub, Pasta, Salad, Dinner_Platter, Shopping_Cart_Item

# Register your models here.
admin.site.register(Topping)
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_Platter)
admin.site.register(Shopping_Cart_Item)
