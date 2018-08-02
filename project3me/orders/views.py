from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from orders.models import *
from django.contrib.auth import login, authenticate
from datetime import datetime
from decimal import *
from orders.form import *



total=Decimal(0.00)
totalcart=Decimal(0.00)
totalcarttemp=Decimal(0.00)

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")
#-------------------------------------------------------------------------
def menu(request):
    # Renders page with list of categories

     return render(request, "mainmenu.html")
#-------------------------------------------------------------------------
def pizzachoices(request):
       # Renders page with list of Pizza Choices

     return render(request, "pizzachoices.html")
#-------------------------------------------------------------------------
def menupizza(request):
     #Renders page with list of pizza options along with the topping form

     context = {

       "form": PizzaForm(request.POST),
       "pizza" : Pizza.objects.all()
     }
     return render(request, "menu.html",context)
#-------------------------------------------------------------------------
def menudinner(request):
     # Renders page with list of Dinner Choices
     context = {
       "Dinner" :Dinner.objects.all()
     }
     return render(request, "dinner.html",context)
#-------------------------------------------------------------------------
def menusalad(request):
      # Renders page with list of Salad Choices
     context = {
       "salad" : Salad.objects.all()
     }
     return render(request, "salad.html",context)
#-------------------------------------------------------------------------
def menusub(request):
    # Renders page with list of Sub Choices

     context = {
       "Sub" : Sub.objects.all()
     }
     return render(request, "sub.html",context)
#-------------------------------------------------------------------------
def menupasta(request):
     # Renders page with list of Pasta Choices


     context = {
       "Pasta" : Pasta.objects.all()
     }
     return render(request, "pasta.html",context)
#-------------------------------------------------------------------------
def menupizzasic(request):
     #Renders page with list of sicilian pizza options along with the topping form

     context = {
         "form": PizzaForm(request.POST),
       "pizza" : PizzaSic.objects.all()
     }
     return render(request, "pizzasic.html",context)


#-------------------------------------------------------------------------
def add_to_cart(request,**kwargs):

    username = request.user.username # Retrieves username of current user
    items=kwargs['items'] # Item summary as a string
    price=kwargs['prices'] # Price of item

    cart_instance = Cart.objects.create(Username=username,Items=items,Price=price)
    # cart_instance.Toppings.add(2)
    # cart_instance.save()

    context = {
       "order" : Cart.objects.all().filter(Username=username),
     }

    return render(request, "added.html",context)
#-------------------------------------------------------------------------
def view(request):

    Username = request.user.username # Retrieves username of current user
    order=Orders.objects.all().filter(Username=Username) # Retrieves all orders of current user
    orderall=Orders.objects.all().filter(Username=Username,Status="Ordered")  # Retrieves all pending orders of current user

    global total #Calculates total due by user
    total=0
    for item in orderall:
        total=total+item.Price

    context = {
       "order" : order ,
        "total":total
    }

    return render(request, "order.html",context)
#-------------------------------------------------------------------------
def viewcart(request):

    global totalcarttemp
    totalcarttemp=Decimal(0.00)
    Username = request.user.username # Retrieves username of current user
    cart = Cart.objects.all().filter(Username=Username)

    for item in cart:
        totalcarttemp=item.Price + totalcarttemp  #Calculates total of items in cart

    context = {
       "cart" : Cart.objects.all().filter(Username=Username),
       "total" :totalcarttemp
     }

    return render(request, "cart.html",context)
#-------------------------------------------------------------------------
def add_to_order(request):
    username = request.user.username # Retrieves username of current user
    cart=Cart.objects.all().filter(Username=username) # Retrieves items in cart of current user
    order=Orders.objects.all().filter(Username=username) # Retrieves orders of current user
    ordernow=Orders.objects.all().filter(Username=username,Status="Ordered") # Retrieves pending orders of current user
    global total
    global totalcart


    for item in cart:
        order_instance = Orders.objects.create(Username=username,Items=item.Items,Price=item.Price,Date=datetime.now(),Status="Ordered")
        global totalcart
        totalcart=totalcart+item.Price  #Calculates total of items in cart


    total=total+totalcart  #Calculates total of order

    for item in cart:
        cart=Cart.objects.all().filter(Username=username).delete() #Clears cart
        totalcart=0 # Resets carts total


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
    ''' Shows entire order history of user'''
    Username = request.user.username
    context = {
       "orders" : Orders.objects.all()
     }

    return render(request, "ordersummary.html",context)
#-------------------------------------------------------------------------
def about(request):
    #Renders page with contact info

    return render(request, "about.html",)
#-------------------------------------------------------------------------
def checkout(request):
    ''' Confirms order with user'''
    global totalcarttemp
    totalcarttemp=Decimal(0.00)

    Username = request.user.username # Retrieves username of current user
    cart = Cart.objects.all().filter(Username=Username) # Retrieves items in cart of current user

    for item in cart:
        totalcarttemp=item.Price + totalcarttemp #Calculates total of items in cart

    context = {
       "cart" : Cart.objects.all().filter(Username=Username), #Calculates total of items in cart
       "total" :totalcarttemp
     }

    return render(request, "checkout.html",context)

def deletecart(request):

    username = request.user.username # Retrieves username of current user

    Cart.objects.filter(Username=username).delete()

    return render(request, "deleted.html")
