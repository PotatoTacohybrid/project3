from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validate_username', views.validate_username, name="validate_username"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('add_to_shopping_cart', views.add_to_shopping_cart, name='add_to_shopping_cart'),
    path('cart', views.cart_view, name="cart"),
    path('logout', views.logout_view, name='logout')
]
