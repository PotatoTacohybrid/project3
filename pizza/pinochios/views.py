from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render
from django.urls import reverse

import sys


from .models import Topping, Regular_Pizza, Sicilian_Pizza, Sub, Pasta, Salad, Dinner_Platter, Shopping_Cart_Item

# Create your views here.
def index(request):
    user = request.user
    if user is None:
        return render(reserve('login_view'))
    amount = Shopping_Cart_Item.objects.filter(user_id=user.id).count()

    context = {
        "amount": amount,
        "regular_pizzas": Regular_Pizza.objects.all(),
        "sicilian_pizzas": Sicilian_Pizza.objects.all(),
        "pastas": Pasta.objects.all(),
        "user_id": user.id
    }
    return render(request, "pinochios/index.html", context)


def login_view(request):
    # If user visited this url
    if request.method == "GET":
        return render(request, 'pinochios/login.html')

    # When logging users in 
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

def register_view(request):
    # If user visited this url
    if request.method == "GET":
        return render(request, 'pinochios/register.html')

    # When registering new user
    else:
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            return Http404('You either disabled javascript like a cheeky monkey or I just donked up') 

        password = request.POST['password']

        if not username or not password:
            return Http404('Please don\' disable javascript')

        # This registers new user without going through django's password requirements
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return Http404('I have no idea what went wrong')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def cart_view(request):
    user = request.user
    if not user:
        return render(request, 'login.html')


    if request.method == "GET":
        context = {
            'cart': Shopping_Cart_Item.objects.all().filter(user_id=user.id)
        }

        return render(request, 'pinochios/cart.html', context)

# Checks if username is already taken
def validate_username(request):
    username = request.POST['username']
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def add_to_shopping_cart(request):
    user_id = int(request.POST['user_id'])
    name = request.POST['name']
    type_of = request.POST['type']
    price1 = float(request.POST['price1'])
    try:
        price2 = float(request.POST['price2'])
    except KeyError:
        p = Shopping_Cart_Item(user_id=user_id, name=name, type_of=type_of, price=price1)
        p.save()
        data = {
            'success': True
        }
        return JsonResponse(data)
    p = Shopping_Cart_Item(user_id=user_id, name=name, type_of=type_of, small_price=price1, large_price=price2)
    p.save()
    data = {
        'success': True
    }
    return JsonResponse(data)
    
        
        


    


