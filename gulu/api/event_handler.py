from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from dish.models import Dish
from review.models import Review
from deal.models import Deal
from restaurant.models import Restaurant
from user_profiles.models import UserProfile
from event.models import Event
from globals.forms import SignupForm

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest

from gulu.api.handlers import event_handler

PTEST = False
# Create objects
"""
    == Event ==
    No 
    event: {event_id , title ,user_id , date , restaurant_obj }
"""
class get_event_by_uid(event_handler):
    #fields = ('id','title','date',('restaurant',('id',)),('user',('id',)))
    def read (self, request):
        uid = request.GET.get('uid')
        if PTEST:
            uid = 3
        user=get_object_or_404(UserProfile,id=uid)
        events=Event.objects.filter(user=user)
        return events
    def create (self, request):
        uid = request.POST.get('uid')
        if PTEST:
            uid = 3
        user=get_object_or_404(UserProfile,id=uid)
        events=Event.objects.filter(user=user)
        return events
    

class create_event(event_handler):
    #model = Event
    #fields = ('id','title','date',('restaurant',('id',)),('user',('id',)))
    #curl -d 'rid=3' -d 'title=cool' -d 'date=123' -d 'uid=4' http://localhost:8000/gulu_api/create_event
    def read (self, request):
        return HttpResponseBadRequest({ 'errorMessage':1 }) #error        
    def create (self, request):
        rid = request.POST.get('rid')
        restaurant_name = request.POST.get('restaurant_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        region = request.POST.get('region')        
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        description='Good Restaurant'
        
        uid = request.POST.get('uid')
        title = request.POST.get('title')
        date = request.POST.get('date')        
        
        if rid and uid and title and date:
            if rid==-1:
                if restaurant_name and latitude and longitude and address and phone and city and region:
                    restaurant = Restaurant(name=restaurant_name,address=address,city=city,region=region,
                                    phone=phone,description=description,latitude=latitude,longitude=longitude)
                    restaurant.save()
                else:
                    return rc.BAD_REQUEST                                    
            else:                
                restaurant=get_object_or_404(Restaurant, id=rid)
            
            user=get_object_or_404(UserProfile,id=uid)
            event_o = Event(title=title,date=date,user=user,restaurant=restaurant)
            event_o.save()
            return event_o            
        else:
            return rc.BAD_REQUEST 
        
class update_event(event_handler):
    #curl -d 'rid=3' -d 'title=usu' -d 'date=123' -d 'eid=1' http://localhost:8000/gulu_api/update_event
    def read (self, request):
        return HttpResponseBadRequest({ 'errorMessage':1 }) #error        
    def create (self, request):
        eid = request.POST.get('eid')
        rid = request.POST.get('rid')                
        title = request.POST.get('title')
        date = request.POST.get('date')                
        if eid and rid and title and date:            
            restaurant=get_object_or_404(Restaurant, id=rid)
            event_o=get_object_or_404(Event, id=eid)            
            event_o.title = title
            event_o.date = date
            event_o.restaurant = restaurant
            event_o.save()
            return event_o
        else:
            return rc.BAD_REQUEST 
