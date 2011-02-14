""" Gulu other locations module views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 435 2010-12-22 08:58:57Z ben $"

from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

from restaurant.models import Restaurant
from globals.utils import slugreverse
from locations.models import other_locations_for, OtherLocationInvitation
from locations.forms import OtherLocationInviteForm

def restaurant_other_locations(request, restaurant_id):
	""" Restaurant other locations index view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	other_locations = other_locations_for(restaurant)
	requests_to = OtherLocationInvitation.objects.filter(to_restaurant=restaurant, status=OtherLocationInvitation.STATUS_SENT)
	requests_from = OtherLocationInvitation.objects.filter(from_restaurant=restaurant)
	
	return render_to_response('locations_restaurant_other_locations.html', {
		'restaurant': restaurant,
		'other_locations': other_locations,
		'requests_to': requests_to,
		'requests_from': requests_from,
	}, context_instance = RequestContext(request))

@login_required
def restaurant_add_other_location(request, restaurant_id):
	""" Restaurant create additional other locations view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	
	if request.method == "POST":
		form = OtherLocationInviteForm(restaurant, request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(slugreverse(restaurant, "restaurant-other-locations", args=[restaurant.id]))
	else:
		form = OtherLocationInviteForm(restaurant)
	
	return render_to_response('locations_restaurant_add_other_location.html', {
		'restaurant': restaurant,
		'form': form,
	}, context_instance = RequestContext(request))

@login_required
def restaurant_handle_invitation(request, restaurant_id, invitation_id, action):
	""" View to accept or decline invitation """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	invitation = get_object_or_404(OtherLocationInvitation, pk=invitation_id, to_restaurant=restaurant, status=OtherLocationInvitation.STATUS_SENT)
	
	if action == "accept":
		invitation.accept()
	elif action == "decline":
		invitation.decline()
	
	return HttpResponseRedirect(slugreverse(restaurant, "restaurant-other-locations", args=[restaurant.id]))
