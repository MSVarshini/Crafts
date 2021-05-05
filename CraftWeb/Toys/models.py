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