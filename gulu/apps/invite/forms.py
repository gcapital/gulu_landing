""" Gulu invite module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 542 2011-01-12 08:40:05Z gage $"

from django import forms

from invite.models import Invite
#from photos.models import TempPhoto

class CreateInviteForm(forms.ModelForm):
	""" Form used for creating new invites """
	
	invite_choices 	= forms.CharField(widget=forms.HiddenInput(), 
		required=True, error_messages={'required': 'You must invite at least one person.'})
	other_sms 		= forms.CharField(widget=forms.TextInput(attrs={'class':'input_medium'}))
	other_email 	= forms.CharField(widget=forms.TextInput(attrs={'class':'input_medium'}))
	#temp_photo		= forms.ModelChoiceField(TempPhoto.objects.all(), widget=forms.HiddenInput())
	temp_photo_url	= forms.CharField(widget=forms.HiddenInput())
	
	class Meta:
		model = Invite
		fields = ('restaurant', 'title', 'start_time', 'message')
		widgets = {
			'restaurant': forms.HiddenInput(),
			'start_time': forms.HiddenInput(),
		}