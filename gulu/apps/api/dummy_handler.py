from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from dish.models import Dish
from review.models import Review
from deal.models import Deal
from restaurant.models import Restaurant
from user_profiles.models import UserProfile
from event.models import Event
from photos.models import Photo
from wall.models import WallPost
from wall.forms import WallPostForm
from gcomments.models import GComment
from actstream import action
from actstream.models import Action
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest
import time
from datetime import datetime

from api.handlers import restaurant_handler, dish_handler, review_handler


PTEST = True
IMAGE_LARGE = 'image600x400'
IMAGE_MEDIUM = 'image185x185'
IMAGE_SMALL = 'image50x50'

WALL_TYPE = ContentType.objects.get_for_model(WallPost)
USERPROFILE_TYPE = ContentType.objects.get_for_model(UserProfile)
ACTION_TYPE = ContentType.objects.get_for_model(Action)

    
"""Dummy"""    
class get_restaurant_info(restaurant_handler):    
    
    def read (self, request): 
        rid = request.GET.get('rid')
        if PTEST:
            rid = 1
        restaurant=get_object_or_404(Restaurant, id=rid)
        return restaurant  
    
    def create (self, request): 
        rid = request.POST.get('rid')
        if PTEST:
            rid = 1
        restaurant=get_object_or_404(Restaurant, id=rid)
        return restaurant

"""Dummy Function"""
class get_dish_by_term(dish_handler):
    def read(self, request):
        rid = 1
        dishes = Dish.objects.filter(restaurant=rid)
        return dishes
        
    def create(self, request):
        rid = 1
        dishes = Dish.objects.filter(restaurant=rid)
        return dishes
 

"""Dummy Function"""
class get_dish_by_rid_term_type(dish_handler):
    def read(self, request):
        rid = 1
        dishes = Dish.objects.filter(restaurant=rid)
        return dishes
        
    def create(self, request):
        rid = 1
        dishes = Dish.objects.filter(restaurant=rid)
        return dishes
            
"""Dummy Function"""
class get_restaurant_search_by_term_and_dishname(restaurant_handler):    
    def read (self, request):
        return Restaurant.objects.all()        
            
    def create (self, request):
        return Restaurant.objects.all()        

"""Dummy Function"""
class get_restaurant_search(restaurant_handler):    
    def read (self, request):
        return Restaurant.objects.all()        
            
    def create (self, request):        
        return Restaurant.objects.all()
        
"""Dummy Function"""
class create_review(review_handler):
    #fields = ('id', 'dish','user','content','created',('photo',(IMAGE_SMALL,IMAGE_MEDIUM,IMAGE_LARGE,'id')))    
    def read (self, request):
        uid = request.GET.get('uid')
        if PTEST:
            uid = 4
            review = Review.objects.filter(user=uid)[0]
            return review
        else:
            raise Http404
            
    def create (self, request):
        uid = request.POST.get('uid')
        if PTEST:
            uid = 4
            review = Review.objects.filter(user=uid)[0]
            return review
        else:
            raise Http404

