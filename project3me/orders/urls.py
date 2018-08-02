from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path("about",views.about, name="about"),
    path("ordersummary",views.ordersummary, name="ordersummary"),
    path("order",views.add_to_order, name="order"),
    path('signup', views.signup, name='signup'),
    path("cart",views.viewcart, name="cart"),
    path("checkout",views.checkout, name="checkout"),
    path("view",views.view, name="view"),
    path("add/<str:items>(?P<prices>\d+\.\d+)<str:top>$",views.add_to_cart, name="add"),
    path("menu", views.menu, name="menu"),
    path("menupizza", views.menupizza, name="menupizza"),
    path("menupizzasic", views.menupizzasic, name="menupizzasic"),
    path("menupasta", views.menupasta, name="menupasta"),
    path("pizzachoices", views.pizzachoices, name="pizzachoices"),
    path("menusub", views.menusub, name="menusub"),
    path("menusalad", views.menusalad, name="menusalad"),
    path("menudinner", views.menudinner, name="menudinner"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("pizzachoices", views.pizzachoices, name="pizzachoices"),

    ]
