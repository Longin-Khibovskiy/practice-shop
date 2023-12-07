from django import forms
from django.forms import NumberInput


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.HiddenInput()
    )