from django.db import models

# Create your models here.
class Customer(models.Model):
	FirstName=models.CharField(max_length=20,unique=True)
	LastName=models.CharField(max_length=20)
	Mobile=models.CharField(max_length=10)
	Email = models.EmailField(blank=True)
	Password = models.CharField(max_length=10,null=True)

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
class Product(models.Model):
	Name=models.CharField(max_length=20,unique=True)
	Image = models.ImageField(upload_to='images/',unique=True)
	Price=models.IntegerField()
	Category=models.CharField(max_length=20)
	Description = models.CharField(max_length=50,blank=True)
	Quantity = models.IntegerField()