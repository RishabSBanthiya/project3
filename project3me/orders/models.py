from django.db import models
from datetime import datetime


class Toppings(models.Model):
    Pepperoni="Pepporoni"
    Sausage="Sausage"

    Topping_Choices=(
        (Pepperoni,'Pepperoni'),
        (Sausage,'Sausage')
        )

    Topps = models.CharField(
        max_length=64,
        choices=Topping_Choices,
    )

    def __str__(self):
        return f"{self.Topps}"
#-------------------------------------------------------------------------
class Pizza(models.Model):
    Regular='RG'
    Sicilian='SC'
    TYPE_CHOICES=(
        (Regular,'Regular'),
        (Sicilian,'Sicilian' )
        )
    Small='SM'
    Large='LG'
    TYPE_CHOICES=((Regular,'Regular'),(Sicilian,'Sicilian') )
    SIZE_CHOICES=(
        (Small,'Small'),
        (Large,'Large'))
    Cheese='Cheese'
    first="1"
    second='2'
    third='3'
    fourth='4'
    fifth='5'
    Special='SPECIAL'
    NUM_TOPPING_CHOICES=(
    (Cheese,'Cheese'),
    (first,'1'),
    (second,'2'),
    (third,'3'),
    (fourth,'4'),
    (fifth,'5'),
    (Special,'SPECIAL'))

    PizzaDish = models.CharField(
        choices=TYPE_CHOICES,
        default=Regular,
        max_length=64,
    )

    Size=models.CharField(
        choices=SIZE_CHOICES,
        default=Small,
        max_length=64,
        )

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    Num_Toppings = models.CharField(
        max_length=64,
        choices=NUM_TOPPING_CHOICES,
        )



    def __str__(self):
        return f"{self.PizzaDish} {self.Size} {self.Num_Toppings}"

#-------------------------------------------------------------------------
class Pasta(models.Model):

    PastaDish=models.CharField( max_length = 64)

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    def __str__(self):
        return f"{self.PastaDish} {self.Price}"
#-------------------------------------------------------------------------
class Sub(models.Model):
    Small='SM'
    Large='LG'
    Cheese='CH'
    NoCheese='NCH'
    SIZE_CHOICES=(
        (Small,'Small'),
        (Large,'Large'))
    CHEESE_CHOICES=(
        (Cheese,'Cheese'),
        (NoCheese,'NoCheese'),
        )
    Sub=models.CharField(max_length=64)

    Size=models.CharField(
        max_length=64,
        choices=SIZE_CHOICES,
        )

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    def __str__(self):
        return f"{self.Sub} {self.Size} {self.Cheese} {self.Price}"
#-------------------------------------------------------------------------
class Dinner(models.Model):
    Small='SM'
    Large='LG'
    SIZE_CHOICES=(
        (Small,'Small'),
        (Large,'Large'))

    Dinner=models.CharField(max_length=64)

    Size=models.CharField(
        max_length=64,
        choices=SIZE_CHOICES,
        )

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    def __str__(self):
        return f"{self.Dinner} {self.Size} {self.Price}"
#-------------------------------------------------------------------------
class Salad(models.Model):

    Salad=models.CharField( max_length=64)

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    def __str__(self):
        return f"{self.Salad} {self.Price}"

#-------------------------------------------------------------------------
class Orders(models.Model):

    Username=models.CharField( max_length=64)
    Items=models.TextField()
    Status=models.TextField(default="Ordered")
    Date=models.DateField(datetime.now())
    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    Toppings=models.ManyToManyField(Toppings,blank = True,)




    def __str__(self):
        return f" {self.Username} {self.Items} {self.Status} {self.Toppings.all()}"
#-------------------------------------------------------------------------

class Cart(models.Model):

    Username=models.CharField( max_length=64)
    Items=models.TextField()
    Status=models.TextField(default="In Cart")
    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )
    Toppings=models.ManyToManyField(Toppings,null=True)


    def __str__(self):
        return f" {self.Username} {self.Items} {self.Status} "

#-------------------------------------------------------------------------z


class PizzaSic(models.Model):
    Regular='RG'
    Sicilian='SC'
    TYPE_CHOICES=(
        (Regular,'Regular'),
        (Sicilian,'Sicilian' )
        )
    Small='SM'
    Large='LG'
    TYPE_CHOICES=((Regular,'Regular'),(Sicilian,'Sicilian') )
    SIZE_CHOICES=(
        (Small,'Small'),
        (Large,'Large'))
    Cheese='Cheese'
    first="1"
    second='2'
    third='3'
    fourth='4'
    fifth='5'
    Special='SPECIAL'
    NUM_TOPPING_CHOICES=(
    (Cheese,'Cheese'),
    (first,'1'),
    (second,'2'),
    (third,'3'),
    (fourth,'4'),
    (fifth,'5'),
    (Special,'SPECIAL'))

    PizzaDish = models.CharField(
        choices=TYPE_CHOICES,
        default=Regular,
        max_length=64,
    )

    Size=models.CharField(
        choices=SIZE_CHOICES,
        default=Small,
        max_length=64,
        )

    Price=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
        )

    Num_Toppings = models.CharField(
        max_length=64,
        choices=NUM_TOPPING_CHOICES,
        )



    def __str__(self):
        return f"{self.PizzaDish} {self.Size} {self.Num_Toppings}"