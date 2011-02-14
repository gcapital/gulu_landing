""" Gulu dish module views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 585 2011-01-27 04:29:41Z jason $"

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from deal.models import Deal
from restaurant.models import Restaurant
from locations.models import other_locations_for
from globals.utils import slugreverse
from deal.forms import AddEditDealForm
from photos.forms import *

def deals(request, restaurant_id):
	""" Deals index view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	deals = Deal.objects.filter(restaurants = restaurant_id)
	return render_to_response('deal_deals.html', {
		'restaurant': restaurant,
		'deals':deals,
	}, context_instance = RequestContext(request))
	
	
def view_deal(request, restaurant_id, deal_id):
	""" Deal detail view """

	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	deal = get_object_or_404(Deal, restaurants=restaurant, pk=deal_id)
	
	return render_to_response('deal_view_deal.html', {
		'restaurant': restaurant,
		'deal': deal,
	}, context_instance = RequestContext(request))

@login_required
def add_deal(request, restaurant_id):
	""" Add deal view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	other_locations = other_locations_for(restaurant)
	other_locations.add(restaurant)
	
	if request.method == 'POST':
		form = AddEditDealForm(request.POST, request.FILES)
		if form.is_valid():
			deal = form.save(commit=False)
			deal.user = request.user
			deal.restaurant = restaurant
			deal.save()
			form.save_m2m()
			return HttpResponseRedirect(slugreverse(restaurant, "deal-deals", args=[restaurant.id]))
	else:
		form = AddEditDealForm()
		
	return render_to_response('deal_add_deal.html', {
		'restaurant': restaurant,
		'other_locations': other_locations,
		'form': form,
	}, context_instance = RequestContext(request))

@login_required	
def edit_deal(request, restaurant_id, deal_id):
	""" Edit deal view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	deal = get_object_or_404(Deal, restaurant=restaurant, pk=deal_id)
	
	if request.method == 'POST':
		form = AddEditDealForm(request.POST, instance=deal)
		if form.is_valid():
			deal = form.save()
			return HttpResponseRedirect(slugreverse(restaurant, "deal-view-deal", args=[restaurant.id, deal.id]))	
	else:
		form = AddEditDealForm(instance=deal)
	
	return render_to_response('deal_edit_deal.html', {
		'restaurant': restaurant,
		'deal': deal,
		'form': form,
	}, context_instance = RequestContext(request))