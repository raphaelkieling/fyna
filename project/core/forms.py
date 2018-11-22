from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('description', 'value','initial_date', 'final_date', 'is_renda', 'tag')