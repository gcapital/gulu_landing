""" Gulu invite module forms """

__author__ = "Jason Ke <u912538@gmail.com>"
__version__ = "$Id: forms.py 570 2011-01-26 07:39:21Z gage $"

from django import forms
from review.models import Review

class CreateReviewForm(forms.ModelForm):
	""" Form used for creating new reviews """
	
	photo_id		= forms.IntegerField(widget=forms.HiddenInput(), required=False)
	photo_url		= forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Review
		fields = ('restaurant', 'user', 'content', 'dish', 'title')
		widgets = {
			'user': forms.HiddenInput(),
			'restaurant': forms.HiddenInput(),
			'dish': forms.HiddenInput(),
			'content': forms.Textarea(),
		}
