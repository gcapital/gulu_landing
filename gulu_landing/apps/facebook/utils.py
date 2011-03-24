from django.contrib.auth import authenticate, login

from facebook.models import FacebookProfile

def login_fb_user(request, facebook_id):
    """ Logs in a User using facebook authentication, returns True 
    if successful, False otherwise """
    
    auth_user = authenticate(facebook_id=facebook_id)
    if not auth_user:
        return False
    login(request, auth_user)
    return True
