from django import forms
from .models import *


class BeanForm(forms.ModelForm):
    class Meta:
        model = Bean
        fields = "__all__"

class RoastForm(forms.ModelForm):
    class Meta:
        model = Roast
        fields = "__all__"

class SyrupForm(forms.ModelForm):
    class Meta:
        model = Syrup
        fields = "__all__"

class PowderForm(forms.ModelForm):
    class Meta:
        model = Powder
        fields = "__all__"

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = "__all__"
        exclude = ['user',]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["date"]
        widgets = {
        'date':forms.DateInput(attrs={"type":'date'}),
        }

class SearchForm(forms.Form):
    date = forms.DateField(widget = forms.DateInput(attrs={"type":"date"}))
