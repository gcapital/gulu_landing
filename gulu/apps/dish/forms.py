""" Gulu dish module forms """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: forms.py 431 2010-12-22 05:29:04Z gage $"

from django import forms
from dish.models import Dish

class AddEditDishForm(forms.ModelForm):
    """ Form used for creating and editing dishes """
    
    temp_photo = forms.IntegerField(widget=forms.HiddenInput);
        
    class Meta:
        model = Dish
        fields = (
        	'name',
        	'vip_price',
        	'price',
        	'description',
        	'type',
        	'reserve',
        	'sale_out',
        	'special',
        	'active',
        )

