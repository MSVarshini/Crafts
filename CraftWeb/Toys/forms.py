from django.forms import ModelForm
from .models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name','Image','Price','Category','Description','Quantity']
        widgets = {
        #'Image': forms.FileInput(attrs={'class':' btn'}),
        'Name': forms.TextInput(attrs = {'class' : 'form-control' } ),
        'Price' : forms.TextInput(attrs = {'class' : 'form-control'} ),
        'Category' : forms.TextInput(attrs = {'class' : 'form-control'} ),
        'Description' : forms.TextInput(attrs = {'class' : 'form-control'} ),
        'Quantity' : forms.TextInput(attrs = {'class' : 'form-control'} ),
        }
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'