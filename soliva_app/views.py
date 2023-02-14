from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from soliva_app.forms import *
from soliva_app.models import Customer
from django.http import HttpResponse


class AppView(SessionWizardView):
	form_list = [CustomerForm, CarForm, AddressForm]
	template_name = "form.html"
	url_name = ""
	done_step_name = ""
	
	def done(self, form_list, **kwargs):
		cus = form_list[0]
		car = form_list[1]
		add = form_list[2]
		if add.is_valid():
			add_obj = add.save()
		if car.is_valid():
			car.save()
		if cus.is_valid():
			data = cus.cleaned_data
			c = Customer.objects.create(**data, address = add_obj )
			c.save()
		return HttpResponse("Datas are saved in DB")