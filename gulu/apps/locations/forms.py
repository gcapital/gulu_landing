""" Gulu other locations module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 392 2010-12-16 08:52:05Z ben $"

from django import forms

from restaurant.models import Restaurant
from locations.models import *

class RestaurantForm(forms.Form):
    
    def __init__(self, restaurant=None, *args, **kwargs):
        self.restaurant = restaurant
        super(RestaurantForm, self).__init__(*args, **kwargs)

class OtherLocationInviteForm(RestaurantForm):
	
	to_restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all())
	
	def clean(self):
		to_restaurant = self.cleaned_data["to_restaurant"]
		
		if to_restaurant == self.restaurant:
			raise forms.ValidationError(u"Cannot add yourself as other location")
		
		previous_invitations_to = OtherLocationInvitation.objects.invitations(to_restaurant=to_restaurant, from_restaurant=self.restaurant)
		if previous_invitations_to.count() > 0:
			raise forms.ValidationError(u"Already requested to add %s as other location" % to_restaurant.name)
		# check inverse
		previous_invitations_from = OtherLocationInvitation.objects.invitations(to_restaurant=self.restaurant, from_restaurant=to_restaurant)
		if previous_invitations_from.count() > 0:
			raise forms.ValidationError(u"%s has already requested to add you as other location" % to_restaurant.name)
		return self.cleaned_data
	
	def save(self):
		to_restaurant = self.cleaned_data["to_restaurant"]
		ol_invitation = OtherLocationInvitation(from_restaurant=self.restaurant, to_restaurant=to_restaurant, status=OtherLocationInvitation.STATUS_SENT)
		ol_invitation.save()
		return ol_invitation