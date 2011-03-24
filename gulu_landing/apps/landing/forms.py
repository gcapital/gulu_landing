""" gulu-landing forms """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"

from django import forms
from landing.models import Registration

class RegistrationForm(forms.ModelForm):   
    class Meta:
        model = Registration