""" Gulu global forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 422 2010-12-21 08:36:10Z ben $"

from django import forms
from django.db.models import Q

from user_profiles.models import UserProfile

class SignupForm(forms.ModelForm):
	""" User signup form """
	
	email_confirm = forms.EmailField()
	password = forms.CharField(min_length=7, widget=forms.PasswordInput())
	password_confirm = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = UserProfile
		fields = (
			'email', 
			'email_confirm',
			'password',
			'password_confirm',
		)

	def clean(self):
		data = self.cleaned_data
		
		email = data.get("email")
		email_confirm = data.get("email_confirm")
		password = data.get("password")
		password_confirm = data.get("password_confirm")
		
		# check for users with the same username or email
		users = UserProfile.objects.filter(
			Q(email=email) | Q(username=email)
		)
		if len(users) > 0:
			raise forms.ValidationError("This email is already in use.")
		
		if email and email != email_confirm:
			raise forms.ValidationError("Email addresses don't match.")
		
		if password and password != password_confirm:
			raise forms.ValidationError("Passwords don't match.")
		
		return data
	
	