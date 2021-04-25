from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def home(req):
	return render(req,'index.html')
def register(req):
	if req.method=="POST":
		firstName=req.POST['FirstName']
		lastName=req.POST['LastName']
		email=req.POST['Email']
		password=req.POST['Password']
		phone = req.POST['Mobile']
		data=Customer(FirstName=firstName,LastName=lastName,Mobile=phone,Email=email,Password=password)
		data.save()
		messages.success(req,"RECORD SAVED")
		return render(req,'index.html')
	return render(req,'login.html')
def login(req):
	if req.method=="POST":
		username = req.POST['FirstName']
		password = req.POST['Password']
		data = Customer.objects.get(FirstName = username)
		if(data.FirstName == username and data.Password == password):
				return render(req,'index.html')
	return render(req,'login.html')
def cart(req):
	return render(req,'cart.html')
def checkout(req):
	return render(req,'checkout.html')
def contact(req):
	return render(req,'contact.html')
def myAccount(req):
	return render(req,'my-account.html')
def productDetail(req):
	return render(req,'product-detail.html')
def productList(req):
	return render(req,'product-list.html')
def wishlist(req):
	return render(req,'wishlist.html')

