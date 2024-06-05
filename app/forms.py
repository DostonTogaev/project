from django import forms
from app.models import Customers

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ()