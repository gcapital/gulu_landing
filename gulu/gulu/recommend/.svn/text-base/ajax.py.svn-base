""" Gulu recommend module AJAX functions """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id$"

import json

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404

from recommend.models import *

def update(request):
	'''
	type: restaurant or dish
	'''
	
	_type = request.POST.get('type', 'restaurant')
	_id = int(request.POST.get('id', 2))
	_score = int(request.POST.get('score', 1))
	
	if(_type=='restaurant'):
		recommends = RestaurantRecommend.objects.filter(pk=_id)
	else:
		recommends = DishRecommend.objects.filter(pk=_id)
	
	if(len(recommends)>0):
		recommend = recommends[0]
		diff = _score - recommend.score
		
		if(_type=='restaurant'):
			recommend.restaurant.count_recommend += diff
			recommend.restaurant.save()
		else:
			recommend.dish.count_recommend += diff
			recommend.dish.save()
			
		recommend.score = _score
		recommend.save()
		
		return HttpResponse(str(recommend.score))
	

