from django.db import models
from soliva_app.enums import *

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	dob = models.DateField()
	address = models.ForeignKey('Address', on_delete=models.CASCADE)
	phone = models.CharField(max_length=10)
	email = models.EmailField()

class Address(models.Model):
	street_name = models.CharField(max_length=200)
	pincode = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	country_code = models.CharField(max_length=2)

class Car(models.Model):
	model_name = models.CharField(max_length=20, choices=CarModels.choices())
	manufacturing_date = models.DateField()
	manufacturer = models.CharField(max_length=20, choices=Manufacturer.choices())
	colour = models.CharField(max_length=20, choices=Colour.choices())