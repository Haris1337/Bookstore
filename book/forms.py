from django.contrib.auth.models import User
from django import forms
from .models import Book, Purchase

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = ['address',]
