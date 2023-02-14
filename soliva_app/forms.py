from django import forms
from soliva_app.models import *
from soliva_app.enums import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ["first_name", "last_name", "age", "dob", "phone", "email"]
		widgets = {
            'dob' : forms.TextInput(attrs={'type':'date'})
        }

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = "__all__"

class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = "__all__"
		widgets = {
            'manufacturing_date' : forms.TextInput(attrs={'type':'date'})
        }