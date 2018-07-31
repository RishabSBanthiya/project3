from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from orders.models import *
from django.contrib.auth import login, authenticate
from datetime import datetime
from decimal import *
from django.forms import ModelForm


total=Decimal(0.00)
totalcart=Decimal(0.00)
totalcarttemp=Decimal(0.00)

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")
#-------------------------------------------------------------------------
def menu(request):

     return render(request, "mainmenu.html")


def menupizza(request):

     context = {
       "pizza" : Pizza.objects.all()
     }
     return render(request, "menu.html",context)

def menudinner(request):

     context = {
       "Dinner" :Dinner.objects.all()
     }
     return render(request, "dinner.html",context)

def menusalad(request):

     context = {
       "salad" : Salad.objects.all()
     }
     return render(request, "salad.html",context)

def menusub(request):

     context = {
       "Sub" : Sub.objects.all()
     }
     return render(request, "sub.html",context)


def menupasta(request):

     context = {
       "Pasta" : Pasta.objects.all()
     }
     return render(request, "pasta.html",context)


#-------------------------------------------------------------------------
def add_to_cart(request,**kwargs):

    username = request.user.username
    items=kwargs['items']

    cart_instance = Cart.objects.create(Username=username,Items=items)

    context = {
       "order" : Cart.objects.all().filter(Username=username),


     }

    return render(request, "added.html",context)
#-------------------------------------------------------------------------
def view(request):
    Username = request.user.username

    context = {
       "order" : Orders.objects.all().filter(Username=Username)
     }

    return render(request, "order.html",context)
#-------------------------------------------------------------------------
def viewcart(request):
    global totalcarttemp
    totalcarttemp=Decimal(0.00)
    Username = request.user.username
    cart = Cart.objects.all().filter(Username=Username)

    for item in cart:
        totalcarttemp=item.Price + totalcarttemp

    context = {
       "cart" : Cart.objects.all().filter(Username=Username),
       "total" :totalcarttemp
     }

    return render(request, "cart.html",context)
#-------------------------------------------------------------------------
def add_to_order(request):
    for i in range(0):
    cart=Cart.objects.all().filter(Username=username)
    order=Orders.objects.all().filter(Username=username)
    ordernow=Orders.objects.all().filter(Username=username,Status="Ordered")
    global total
    global totalcart


    for item in cart:
        order_instance = Orders.objects.create(Username=username,Items=item.Items,Price=item.Price,Date=datetime.now())
        global totalcart
        totalcart=totalcart+item.Price


    total=total+totalcart

    for item in cart:
        cart=Cart.objects.all().filter(Username=username).delete()
        totalcart=0


    context = {
      "order" :Orders.objects.all().filter(Username=username,Status="Ordered"),
       "total":total
    }

    return render(request, "order.html",context)
#-------------------------------------------------------------------------

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#-------------------------------------------------------------------------
def ordersummary(request):
    Username = request.user.username

    context = {
       "orders" : Orders.objects.all()
     }

    return render(request, "ordersummary.html",context)
#-------------------------------------------------------------------------
def about(request):

    return render(request, "about.html",)

class ToppingForm(ModelForm):
     class Meta:
         model=