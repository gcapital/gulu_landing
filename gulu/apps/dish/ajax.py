""" Gulu dish module AJAX functions """

__author__ = "Gage Tseng<gage.tseng@geniecapital.com>"
__version__ = "$Id:$"

import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from dish.models import Dish
from restaurant.models import Restaurant
from search.ajax import wildcard_search

from haystack.query import SearchQuerySet

def search(request, restaurant_id):
	""" Performs a basic search on GET['q'] and returns results as
	a JSON array """
	
	q = request.GET.get('term', None)
	if q is None or q == '':
		return HttpResponse(json.dumps({'error':'query empty'}), mimetype="application/json")
	
	results = SearchQuerySet().filter(name_ngram=q).models(Dish)
	
	json_response = []
	for result in results:
		item = {
			'id': result.id.split(".")[2],
			'value': result.name,
		}
		json_response.append(item)	
		
	return HttpResponse(json.dumps(json_response), mimetype="application/json")

def get_details(request):
	did = request.GET.get('did', None)
	dish = get_object_or_404(Dish, pk=did)
	
	return render_to_response("inc_dish_details.html", {
		'dish': dish,
	}, context_instance = RequestContext(request))

def show_menu(request):
    '''
    display restaurant menu given a dish type
    '''
    
    dish_type = request.GET.get('dish_type',None)
    restaurant_id = request.GET.get('restaurant_id',None)
    dishes = Dish.objects.filter(restaurant = restaurant_id)
    msg = 'aaa';
    
    if int(dish_type) > 0:
        dishes = dishes.filter(type=dish_type)
        
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    
    menu_list_html = render_to_string('inc_menu_list.html',{
         'dishes': dishes,
         'restaurant' : restaurant,
         'msg' : msg,
    }, context_instance = RequestContext(request))
    
    return HttpResponse(menu_list_html, mimetype="text/html")