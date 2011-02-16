from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from dish.models import Dish, DishType
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
from piston.models import Sync, Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponseBadRequest
from django.template import RequestContext
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

DEFAULT_DISH_PHOTO_ID = 41
DEFAULT_RESTAURANT_PHOTO_ID = 41
DEFAULT_DISH_TYPE_ID = 1

def restaurant_dummy(request):
    r_o = Restaurant.objects.get(id=1)
    r_o.latitude = 25.021708
    r_o.longitude = 121.548179
    r_o.save()
    return render_to_response('facebook_cancel.html', {
                   'site_name' : 'facebook',
                   }, context_instance = RequestContext(request))
    
def doc_dummy(request):
    return redirect("https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0Bz17PwpUHlCIMzE4NDczMGMtYWUwMS00ZjYyLWJjZTEtOWQ2M2YyMmE3YTZl&hl=zh_TW&authkey=CLPH74YO")

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
    #curl -d 'uid=4' -d 'dish_name=perfect test' -d 'did=-1' -d 'rid=1' -d 'review_content=how are you' -d 'photo_id=28' http://localhost:8000/api/create_review
    """ 
    16.taste 
    17.value 
    18.quality 
    19.presentation """    
    def read (self, request):
        uid = request.GET.get('uid')
        
        dish_name = request.GET.get('dish_name')
        did = request.GET.get('did')
        
        rid = request.GET.get('rid')
        restaurant_name = request.GET.get('restaurant_name')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        address = request.GET.get('address')
        phone = request.GET.get('phone')
        city = request.GET.get('city')        
        region = request.GET.get('region')
        
        #photo_name = request.GET.get('photo_name')
        review_content = request.GET.get('review_content')        
        photo_id = request.GET.get('photo_id')        
        taste = request.GET.get('taste')
        value = request.GET.get('value')
        quality = request.GET.get('quality')
        presentation = request.GET.get('presentation')
        #41
        user_o = get_object_or_404(UserProfile, id=uid)
        if rid == '-1':
            main_profile_pic = Photo.objects.get(id=DEFAULT_RESTAURANT_PHOTO_ID)
            restaurant_o = Restaurant(name=restaurant_name,address=address,city=city,region=region,phone=phone,
                                      longitude=longitude,latitude=latitude,main_profile_pic=main_profile_pic)
            restaurant_o.save()
        else: 
            restaurant_o = get_object_or_404(Restaurant, id=rid)
        if did == '-1':
            main_pic = Photo.objects.get(id=DEFAULT_DISH_PHOTO_ID)
            dish_type = DishType.objects.get(id=DEFAULT_DISH_TYPE_ID)
            dish_o = Dish(main_pic=main_pic,restaurant=restaurant_o,name=dish_name,description='New gulu dish',user=user_o,type=dish_type)
            dish_o.save()
        else:
            dish_o = get_object_or_404(Dish,id=did)
        photo_o = get_object_or_404(Photo,id=photo_id)
        review_o = Review(restaurant=restaurant_o,dish=dish_o,user=user_o,photo=photo_o,content=review_content,title="gulu Review by %s"%user_o.get_full_name)
            
        return review_o
            
    def create (self, request):
        uid = request.POST.get('uid')
        
        dish_name = request.POST.get('dish_name')
        did = request.POST.get('did')
        
        rid = request.POST.get('rid')
        restaurant_name = request.POST.get('restaurant_name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')        
        region = request.POST.get('region')
        
        #photo_name = request.POST.get('photo_name')
        review_content = request.POST.get('review_content')        
        photo_id = request.POST.get('photo_id')        
        taste = request.POST.get('taste')
        value = request.POST.get('value')
        quality = request.POST.get('quality')
        presentation = request.POST.get('presentation')
        #41
        user_o = get_object_or_404(UserProfile, id=uid)
        if rid == '-1':
            main_profile_pic = Photo.objects.get(id=DEFAULT_RESTAURANT_PHOTO_ID)
            restaurant_o = Restaurant(name=restaurant_name,address=address,city=city,region=region,phone=phone,
                                      longitude=longitude,latitude=latitude,main_profile_pic=main_profile_pic)
            restaurant_o.save()
        else:             
            restaurant_o = get_object_or_404(Restaurant, id=rid)
        if did == '-1':
            main_pic = Photo.objects.get(id=DEFAULT_DISH_PHOTO_ID)
            dish_type = DishType.objects.get(id=DEFAULT_DISH_TYPE_ID)
            dish_o = Dish(main_pic=main_pic,restaurant=restaurant_o,name=dish_name,description='New gulu dish',user=user_o,type=dish_type)
            dish_o.save()
        else:
            dish_o = get_object_or_404(Dish,id=did)
        photo_o = get_object_or_404(Photo,id=photo_id)
        review_o = Review(restaurant=restaurant_o,dish=dish_o,user=user_o,photo=photo_o,content=review_content,title="gulu Review by %s"%user_o.get_full_name)
        review_o.save()
        
        site_o = Site.objects.get(name = 'facebook')
        sync_o = Sync.objects.get(user=user_o, site = site_o)        
        url = 'https://graph.facebook.com/%s/photos?access_token=%s'%(sync_o.verifier,sync_o.token)
        datagen, headers = multipart_encode({"source": open(photo_o.image.path, "rb"),
                                             'message':review_content.encode('utf-8')})
        req = urllib2.Request(url, datagen, headers)                    
        return review_o
    

