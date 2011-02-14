""" Gulu recommend module views """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: views.py 404 2010-12-17 03:32:45Z de $"

import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings

from recommend.models import RestaurantRecommend, DishRecommend

def index(request, user_id):
    
    restaurant_recommends = RestaurantRecommend.objects.filter(created_user=user_id)
    dish_recommends = DishRecommend.objects.filter(created_user=user_id)
    
    return render_to_response('recommend_index.html', {
        'restaurant_recommends' : restaurant_recommends,
        'dish_recommends'       : dish_recommends,
    }, context_instance = RequestContext(request))
