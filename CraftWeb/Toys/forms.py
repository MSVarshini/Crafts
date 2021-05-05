from django.forms import ModelForm
from .models import *
from django import forms

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']