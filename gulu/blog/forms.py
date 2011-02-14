""" Gulu post module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 388 2010-12-16 06:59:01Z ben $"

from django import forms
from blog.models import RestaurantPost, UserPost

class AddEditRestaurantPostForm(forms.ModelForm):
	""" Form used for adding and editing restaurant blog posts """
	
	class Meta:
		model = RestaurantPost
		fields = ('title', 'content')

class AddEditUserPostForm(forms.ModelForm):
	""" Form used for adding and editing user blog posts """
	
	class Meta:
		model = UserPost
		fields = ('title', 'content')