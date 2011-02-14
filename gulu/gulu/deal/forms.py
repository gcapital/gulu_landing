""" Gulu deal module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 407 2010-12-20 06:11:05Z ben $"

from django import forms

from deal.models import Deal
from restaurant.models import Restaurant

class AddEditDealForm(forms.ModelForm):
	""" Form used for adding and editing deals """
	
	#restaurants = forms.ModelMultipleChoiceField(queryset=Deal.objects.filter())
	
	class Meta:
		model = Deal
		
		fields = (
			'title',
			'type',
			'cover',
			'amount',
			'restaurants',
			'dish',
			'start_datetime',
			'end_datetime',
			'ongoing',
			'conditions',
		)
		widgets = {
			'cover': forms.HiddenInput(attrs={'id':'id_cover_id'}),
		}

	def clean(self):
		cleaned_data = self.cleaned_data
		type = cleaned_data.get('type', None)
		ongoing = cleaned_data.get('ongoing', None)
		start_datetime = cleaned_data.get('start_datetime', None)
		end_datetime = cleaned_data.get('end_datetime', None)
		
		if not ongoing and not start_datetime and not end_datetime:
			raise forms.ValidationError("If not ongoing, must specify a start and/or end date.")
		
		# These types all require an amount
		if type and type in [
			Deal.TYPE_PERCENT_OFF,
			Deal.TYPE_AMOUNT_OFF,
			Deal.TYPE_PERCENT_OFF_DISH,
			Deal.TYPE_AMOUNT_OFF_DISH,
		] and not cleaned_data['amount']:
			raise forms.ValidationError("Must specify an amount for this deal type.")
			
		# These types require a dish
		if type and type in [
			Deal.TYPE_PERCENT_OFF_DISH,
			Deal.TYPE_AMOUNT_OFF_DISH,
			Deal.TYPE_FREE_ITEM,
		] and not cleaned_data['dish']:
			raise forms.ValidationError("Must specify a dish for this deal type.")
			
		return cleaned_data
