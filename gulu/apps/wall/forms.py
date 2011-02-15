""" Gulu wall module forms """

__author__ = "Jason Ke <u912538@gmail.com>"
__version__ = "$Id: forms.py 413 2010-12-21 01:37:01Z jason $"

from django import forms
from django.contrib.contenttypes.models import ContentType

from wall.models import WallPost

class BaseWallPostForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		initial = None
		if 'owner' in kwargs:
			initial = {
				'owner_content_type': ContentType.objects.get_for_model(kwargs['owner']).pk,
				'owner_object_id': kwargs['owner'].id,
			}
			del kwargs['owner']
		super(BaseWallPostForm, self).__init__(initial=initial, *args, **kwargs)

class WallPostForm(BaseWallPostForm):
	photo_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = WallPost
		fields = (
			'content',
			'owner_content_type',
			'owner_object_id',
		)
		widgets = {
			'content': forms.Textarea(attrs={'class':'input6', 'value':'comments'}),
			'owner_content_type': forms.HiddenInput(),
			'owner_object_id': forms.HiddenInput(),
		}
