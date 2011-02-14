""" Gulu restaurant module AJAX functions """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: ajax.py 388 2010-12-16 06:59:01Z ben $"

import json

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404

from restaurant.models import Restaurant

def search_restaurants(request):
	""" Returns a JSON encoded list of restaurant objects, filtered by query
	
	Data is returned in the form:
	
	[
		{
			'id': <restaurant pk>,
			'value': <restaurant name>,
		}
	]
	"""
	
	query = request.GET.get('term', None)
	data = []
	restaurants = Restaurant.objects.filter(name__icontains=query)
	
	for r in restaurants:
		data.append({
			'id': r.pk,
			'value': r.name,
		})
	
	return HttpResponse(json.dumps(data), mimetype="application/json")
	
def get_restaurant_details(request):
	restaurant_id = request.GET.get('rid', None)
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	
	return render_to_response("inc_restaurant_details.html", {
		'restaurant': restaurant,
	}, context_instance = RequestContext(request))

