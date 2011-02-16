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
from globals.forms import SignupForm
from photos.models import Photo
from piston.models import Sync, Site
"""DJANGO LIB"""
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest
from django.core.validators import email_re
from django.contrib.auth import authenticate, login

from api.handlers import user_handler

"""GLOBAL VARIATION"""
DEFAULT_USER_PHOTO_ID = 41
PTEST = False

"""
    == User ==
    No phone, errorMessage, syncArray
    user object:{uid, username, email, phone, errorMessage, syncArray, user_image, about}
                (favorate, dish@place, place)
"""    
class get_user_info(user_handler):    
    def read (self, request):
        uid = request.GET.get('uid')
        if PTEST:
            uid = 3
        user=get_object_or_404(UserProfile,id=uid)
        return user
    
    def create (self, request):
        uid = request.POST.get('uid')
        if PTEST:
            uid = 3
        user=get_object_or_404(UserProfile,id=uid)
        return user
    
class signup_checkusername(BaseHandler):
    def read (self, request):
        username = request.GET.get('username')
        if not username:
            return HttpResponseBadRequest({ 'errorMessage':2 })
        user = UserProfile.objects.filter(username=username)         
        if not user:
            return { 'errorMessage':0 } #available
        else:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #already used
        
    def create (self, request):
        username = request.POST.get('username')
        if not username:
            return HttpResponseBadRequest({ 'errorMessage':2 })
        user = UserProfile.objects.filter(username=username)         
        if not user:
            return { 'errorMessage':0 } #available
        else:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #already used
        

class signup_checkemail(BaseHandler):
    def read (self, request):
        email = request.GET.get('email')
        if not email:
            return HttpResponseBadRequest({ 'errorMessage':2 })
        user = UserProfile.objects.filter(email=email)         
        if not user:
            return { 'errorMessage':0 } #available
        else:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #already used
        
    def create (self, request):
        email = request.POST.get('email')
        if not email:
            return HttpResponseBadRequest({ 'errorMessage':2 })
        user = UserProfile.objects.filter(email=email)         
        if not user:
            return { 'errorMessage':0 } #available
        else:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #already used


"""Profile photo need to modify, and sync_o need to modify too, and slug need to modify...."""
#curl -d 'username=pp' -d 'password=pp' -d 'email=pp@hmail.com' -d 'phone=0099000' http://192.168.11.2:8000/api/signup
class signup(user_handler):
    def read (self, request):
        return HttpResponseBadRequest({ 'errorMessage':1 }) #error
    def create (self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        main_profile_pic = Photo.objects.get(id=DEFAULT_USER_PHOTO_ID)
        facebook_site = Site.objects.get(name='facebook')
        sync_o = Sync(site=facebook_site)        
        if phone and email and password and username:            
            new_user = UserProfile.objects.create_user(username, email, password)
            new_user.phone = phone
            new_user.main_profile_pic = main_profile_pic
            new_user.slug = username
            new_user.first_name = username            
            new_user.save()
            sync_o.user = new_user
            sync_o.save()
            new_user.syncs.add(sync_o)
            sync_o.save()
            return new_user
        else:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #error
        

class signin(user_handler):
    #curl -d 'name_email=gage' -d 'password=gage' -d 'date=123' -d 'eid=1' http://192.168.11.2:8000/api/signin
    def read (self, request):
        return HttpResponseBadRequest({ 'errorMessage':1 }) #error    
    def create (self, request):
        name_email = request.POST.get('name_email')
        password = request.POST.get('password')
        if not name_email:
            return HttpResponseBadRequest({ 'errorMessage':1 }) #error
        if email_re.match(name_email):
            try:
                user_o = get_object_or_404(UserProfile, email=name_email)
            except Http404:
                return HttpResponseBadRequest({ 'errorMessage':1 }) 
        else:
            try:
                user_o = get_object_or_404(UserProfile, username=name_email)
            except Http404:
                return HttpResponseBadRequest({ 'errorMessage':1 })
             
        username = user_o.username
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseBadRequest({'errorMessage':2 })
        return user
    

class upload_user_info(BaseHandler):
    def read (self, request):
        return HttpResponseBadRequest({ 'errorMessage':1 }) #error
    def create (self, request):
        uid = request.POST.get('uid')
        about_text = request.POST.get('about_text')
        user=get_object_or_404(UserProfile, id=uid)
        if request.FILES.get('uploadedfile'):
            photo_obj = Photo(image=request.FILES['uploadedfile'])
            photo_obj.user = user
            photo_obj.save()
            user.main_profile_pic = photo_obj
        if about_text: 
            user.about_me = about_text
        user.save()
        return user
        
        