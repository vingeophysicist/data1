from .models import CustomerInfo, CustomerDocument 
from django.forms import ModelForm
from django import forms



CUSTOMER_CHOICES = [
    ('commercial', 'Commercial'),
    ('private', 'Private'),
]

class CustomerTypeForm(forms.Form):
    customer_chioces = forms.CharField(label="Customertype", widget=forms.RadioSelect(choices=CUSTOMER_CHOICES))
    
class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = "__all__"
    
class CustomerDocumentForm(forms.ModelForm):
    class Meta:
        model = CustomerDocument
        fields = ['document']