""" Gulu photo module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 534 2011-01-11 04:20:28Z ben $"

from django import forms
from django.contrib.contenttypes.models import ContentType

from photos.models import Photo

class PhotoForm(forms.ModelForm):
	
	def __init__(self, content_object=None, edit=False, *args, **kwargs):
		super(PhotoForm, self).__init__(*args, **kwargs)
		
		if edit:
			del self.fields['image']
	
	class Meta:
		model = Photo
		fields = ('image', 'title', 'description')
