"""PISTON LIB"""
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
"""GULU LIB"""
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
from piston.models import Sync
"""DJANGO LIB"""
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest
""""PYTHON LIB"""
import time
from datetime import datetime

"""GLOBAL VARIATION"""
PTEST = False
IMAGE_LARGE = 'image600x400'
IMAGE_MEDIUM = 'image185x185'
IMAGE_SMALL = 'image50x50'

WALL_TYPE = ContentType.objects.get_for_model(WallPost)
USERPROFILE_TYPE = ContentType.objects.get_for_model(UserProfile)
ACTION_TYPE = ContentType.objects.get_for_model(Action)

"""MESSAGE the emitters of main_profile_pic and cover are modified in piston/emitters.py"""
class deal_handler(BaseHandler):
    model = Deal
    fields = ('id','title', 'conditions','restaurant','cover')        
class dish_handler(BaseHandler):
    model = Dish 
    fields = ('name','id', 'restaurant', 'user')
class restaurant_handler(BaseHandler):
    model = Restaurant 
    fields = ('id','name','address','phone','latitude','longitude','city','region', 'managers', 'score', 'main_profile_pic')
class event_handler(BaseHandler):
    model = Event
    fields = ('id','title','date','restaurant','user')
class user_handler(BaseHandler):
    model = UserProfile
    fields = ('id', 'username','email','about_me','phone','main_profile_pic','syncs')
class review_handler(BaseHandler):
    model = Review
    fields = ('id', 'dish','user','content','created','photo')    
class photo_handler(BaseHandler):
    model = Photo
    fields = (IMAGE_SMALL,IMAGE_MEDIUM,IMAGE_LARGE,'id')
class wall_handler(BaseHandler):
    model = WallPost
    fields = ('poster','content','created','id','time_ago','comment_count')
class comment_handler(BaseHandler):
    model = GComment
    fields = ('id','comment','user','submit_date','time_ago','post_id')
class sync_handler(BaseHandler):
    model = Sync
    fields = ('id','type','token','url','icon_url')


"""
    == Dish ==
    fields = ('name','id', 'restaurant', 'user')
"""

class get_dish_by_rid(BaseHandler):    

    def read(self, request):
        rid = request.GET.get('rid')
        if PTEST:
            rid = 1
        dishes = Dish.objects.filter(restaurant=rid)        
        return dishes
    
    def create(self, request):
        rid = request.POST.get('rid')
        if PTEST:
            rid = 1
        dishes = Dish.objects.filter(restaurant=rid)        
        return dishes


class get_dish_nearby(BaseHandler):
    def isFloat(self, para):
        part_para = para.split('.',1)
        for seg in part_para:
            if seg.isdigit()==False:
                return False
        return True                 
    def read (self, request):        
        latitude = str(request.GET.get('latitude'))
        longitude = str(request.GET.get('longitude'))
        
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        rests = Restaurant.objects.all()    
        dish_list=[]
        for each_rest in rests:
            if each_rest.longitude<=longitude+0.3 and each_rest.longitude>=longitude-0.3 and each_rest.latitude<=latitude+0.3 and each_rest.latitude>=latitude-0.3:
                near_dish = Dish.objects.filter(restaurant=each_rest)
                for each_dish in near_dish:
                    dish_list.append(each_dish)             
        return dish_list
    
    def create (self, request):        
        latitude = str(request.POST.get('latitude'))
        longitude = str(request.POST.get('longitude'))
        
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        rests = Restaurant.objects.all()
        dish_list=[]
        for each_rest in rests:
            if each_rest.longitude<=longitude+0.3 and each_rest.longitude>=longitude-0.3 and each_rest.latitude<=latitude+0.3 and each_rest.latitude>=latitude-0.3:
                near_dish = Dish.objects.filter(restaurant=each_rest)
                for each_dish in near_dish:
                    dish_list.append(each_dish)                
        return dish_list
"""
    == Review ==
    fields = ('id', 'dish','user','content','created','photo') 
"""    
class get_review_by_uid(BaseHandler):    
    
    def read(self, request):
        uid = request.GET.get('uid')
        if PTEST:
            uid = 4
        reviews = Review.objects.filter(user=uid)[:10]
        return reviews
    
    def create(self, request):
        uid = request.POST.get('uid')
        if PTEST:
            uid = 4
        reviews = Review.objects.filter(user=uid)[:10]
        return reviews
    
class get_review_by_rid(BaseHandler):    
    
    def read(self, request):
        rid = request.GET.get('rid')
        if PTEST:
            rid = 1
        reviews = Review.objects.filter(restaurant=rid)[:10]        
        return reviews
        
    def create(self, request):
        rid = request.POST.get('rid')
        if PTEST:
            rid = 1
        reviews = Review.objects.filter(restaurant=rid)[:10]
        return reviews
"""
    == Deal ==
    fields = ('id','title', 'conditions','restaurant','cover')
"""
class get_deal_by_rid(BaseHandler):    
        
    def read(self, request):
        rid = request.GET.get('rid')
        if PTEST:
            rid = 1
        deals = Deal.objects.filter(restaurant=rid)
        return deals
    def create(self, request):
        rid = request.POST.get('rid')
        if PTEST:
            rid = 1
        deals = Deal.objects.filter(restaurant=rid)
        return deals

class get_deal_nearby(BaseHandler):

    def isFloat(self, para):
        part_para = para.split('.',1)
        for seg in part_para:
            if seg.isdigit()==False:
                return False
        return True         
           
    def read(self, request):
        latitude = str(request.GET.get('latitude'))
        longitude = str(request.GET.get('longitude'))
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        deals = Deal.objects.all()
        deal_list = []
        for each_deal in deals:
            deal_rest = each_deal.restaurant
            if deal_rest.longitude<=longitude+0.3 and deal_rest.longitude>=longitude-0.3 and deal_rest.latitude<=latitude+0.3 and deal_rest.latitude>=latitude-0.3:
                deal_list.append(each_deal)
        return deal_list
    
    def create(self, request):
        latitude = str(request.POST.get('latitude'))
        longitude = str(request.POST.get('longitude'))
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        deals = Deal.objects.all()
        deal_list = []
        for each_deal in deals:
            deal_rest = each_deal.restaurant
            if deal_rest.longitude<=longitude+0.3 and deal_rest.longitude>=longitude-0.3 and deal_rest.latitude<=latitude+0.3 and deal_rest.latitude>=latitude-0.3:
                deal_list.append(each_deal)
        return deal_list    
"""
    == Restaurant ==
    fields = ('id','name','address','phone','latitude','longitude','city','region', 'managers', 'score', 'main_profile_pic')
"""
class get_restaurant_nearby(BaseHandler):    

    def isFloat(self, para):
        part_para = para.split('.',1)
        for seg in part_para:
            if seg.isdigit()==False:
                return False
        return True                 
    def read (self, request):        
        latitude = str(request.GET.get('latitude'))
        longitude = str(request.GET.get('longitude'))
        
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        rests = Restaurant.objects.all()
        rest_list = []
        for each_rest in rests:
            if each_rest.longitude<=longitude+0.3 and each_rest.longitude>=longitude-0.3 and each_rest.latitude<=latitude+0.3 and each_rest.latitude>=latitude-0.3:
                rest_list.append(each_rest)                
        return rest_list
    
    def create (self, request):        
        latitude = str(request.POST.get('latitude'))
        longitude = str(request.POST.get('longitude'))
        
        if PTEST:
            longitude = '0.0'
            latitude = '0.0'         
        if self.isFloat(latitude) and self.isFloat(longitude):            
            latitude = float(latitude)
            longitude = float(longitude)
        else:
            return []                
        rests = Restaurant.objects.all()
        rest_list = []
        for each_rest in rests:
            if each_rest.longitude<=longitude+0.3 and each_rest.longitude>=longitude-0.3 and each_rest.latitude<=latitude+0.3 and each_rest.latitude>=latitude-0.3:
                rest_list.append(each_rest)                
        return rest_list


class create_photo(BaseHandler):
    fields = (IMAGE_SMALL,IMAGE_MEDIUM,IMAGE_LARGE,'id')
    def read (self, request):
        return HttpResponseBadRequest({'errorMessage':1 }) 
    def create (self, request): 
        uid = request.POST.get('uid')
        description = request.POST.get('description')
        title = request.POST.get('title')
        if PTEST:
            uid = 4 #gage
            description = 'some desciption'
            title = 'some title'
        user=get_object_or_404(UserProfile, id=uid)
        if not request.FILES.get('uploadedfile'):
            return HttpResponseBadRequest({ 'errorMessage':1 }) #error
        photo_obj = Photo(image=request.FILES['uploadedfile'],description=description,title=title)
        photo_obj.user = user
        photo_obj.save()
        return photo_obj

