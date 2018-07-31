from django.contrib import admin

# Register your models here.
from .models import Pizza,Pasta,Sub,Salad,Dinner,Orders
admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(Salad)
admin.site.register(Dinner)
admin.site.register(Orders)
