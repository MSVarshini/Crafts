from django.shortcuts import render,redirect
from .models import *

# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
# Create your views here.

def home(req):
	return render(req,'index.html')
def requestProduct(req):
	return render(req,'requestProduct.html')
# def register1(req):
# 	form = CreateUserForm()
# 	context = {'form': form}
# 	if req.method == 'POST':
# 		form = CreateUserForm(req.POST)
# 		if form.is_valid():
# 			form.save()
# 	return render(req,'register1.html',context)
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
	if req.method == 'GET':
		products = Hotel.objects.all()
		return render(req, 'prod.html',{'Images' : products})
def paintings(req):
	if req.method == 'GET':
		products = Product.objects.filter(Category = "paintings")
		print(products)
		return render(req, 'prod.html',{'Images' : products})
def kondapalli(req):
	if req.method == 'GET':
		products = Product.objects.filter(Category = "kondapalli")
		print(products)
		return render(req, 'prod.html',{'Images' : products})
def bottleArts(req):
	if req.method == 'GET':
		products = Product.objects.filter(Category = "bottleArt")
		print(products)
		return render(req, 'prod.html',{'Images' : products})

def wishlist(req):
	return render(req,'wishlist.html')

def hotel_image_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()
    return render(request, 'uploadProduct.html', {'form' : form})  
def success(request):
    return HttpResponse('successfully uploaded')

def Edit(req):
	return render(req , 'EditProfile.html')
