from django import forms
from .models import Order
from datetime import datetime

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'address': 'Адрес',
            'postal_code': 'Почтовый индекс',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'address': forms.TextInput(attrs={'class': 'input'}),
            'postal_code': forms.TextInput(attrs={'class': 'input'}),
        }


class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    cardholder_name = forms.CharField(label='Cardholder Name', max_length=100)
    expiration_date = forms.DateField(label='Expiration Date')
    cvv = forms.IntegerField(label='cvv')

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        # Additional validation for the card number
        if len(card_number) != 16:
            raise forms.ValidationError("Invalid card number.")
        return card_number

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        # Additional validation for the expiration date
        datetime_obj = datetime.now()  # datetime.datetime object
        date_obj = datetime_obj.date()
        if expiration_date <= date_obj:
            raise forms.ValidationError("Invalid expiration date.")
        return expiration_date

    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        # Additional validation for the CVV
        if cvv < 100 or cvv > 999:
            raise forms.ValidationError("Invalid CVV.")
        return cvv
