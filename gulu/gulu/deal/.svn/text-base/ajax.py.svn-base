""" Gulu deal module AJAX functions """

__author__ = "Jason Ke<jason.ke@geniecapital.com>"
__version__ = "$Id$"

import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from restaurant.models import Restaurant
from deal.models import Deal

def deal_view_single(request):
	deal_id = request.POST.get('deal_id',None)
	deal = get_object_or_404(Deal, pk=deal_id)
	
	data = render_to_string('inc_deal_single.html',{
		'deal': deal,
	}, context_instance = RequestContext(request))
	    
	return HttpResponse(data, mimetype="text/html")