from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

from facebook.facebook_api import FacebookAPI
from facebook.graph_api import get_user_from_cookie
from facebook.utils import login_fb_user

from landing.models import Registration

def connect(request):
    """ Facebok-based signup/login """
    
    fb_user = get_user_from_cookie(request.COOKIES, 
        settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
    if not fb_user:
        return redirect('registration-signup')
    fb = FacebookAPI(fb_user['access_token'])
    
    # make sure the token is actually valid
    if not fb.is_authenticated():
        return redirect('/')
    
    Registration.objects.create(email=fb.get_profile()['email'])
    messages.info(request, "Thanks for signing up.  We'll let you know when the beta " \
        "is available")
    
    # TODO: Is this really the desired redirect?
    return redirect('/')