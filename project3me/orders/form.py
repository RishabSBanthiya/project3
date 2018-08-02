from django import forms
from orders.models import *

class PizzaForm (forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ["Items","Username","Status","Price"]
        # exclude = ["Username"]
        # exclude = ["Price"]
        # exclude = ["Status"]

    def __init__ (self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        # self.fields["Toppings"].widget = forms.widgets.CheckboxSelectMultiple()
