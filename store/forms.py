from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms



from .models import Feedback, Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ContactUs(forms.ModelForm):
    name = forms.CharField(label="Enter first name")
    email = forms.CharField()
    mobile_no = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = '__all__'

    
