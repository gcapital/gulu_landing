""" Gulu globals module forms """

__author__ = "Jason Ke <jason.ke@geniecapital.com>"
__version__ = "$Id: forms.py 388 2010-12-16 06:59:01Z jason $"

from django import forms
from django.db import models

from globals.models import NewsletterUser

class CreateNewsletterForm(forms.ModelForm):
	""" Form used for creating newsletter input fields """
	

	class Meta:
		model = NewsletterUser
		fields = ('username', 'email')
		username 	= models.CharField()
		email 		= models.EmailField()

		widgets = {
			'username': forms.TextInput(attrs={'class': 'username','value':'User name you want on gulu'}),
			'email': forms.TextInput(attrs={'class': 'email', 'value':'Email'}),
		}
