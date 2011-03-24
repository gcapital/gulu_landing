import datetime
import string
from random import choice

from django.contrib.auth.models import User

from facebook.graph_api import GraphAPI, GraphAPIError
from facebook.models import FacebookProfile

class FacebookAPIError(Exception):
    pass


class FacebookNotAuthenticated(FacebookAPIError):
    pass


class FacebookAPI(GraphAPI):
    """ Gulu facebook API wrapper """
    def __init__(self, access_token=None):
        self._is_authenticated = None
        self._profile = None
        self.access_token = access_token
        if self.access_token:
            GraphAPI.__init__(self, access_token)

    def is_authenticated(self):
        """ Checks if the cookie/post data provided is actually valid """
        if self._is_authenticated is None:
            try:
                self.get_profile()
                self._is_authenticated = True
            except GraphAPIError, e:
                self._is_authenticated = False
        return self._is_authenticated

    def get_profile(self):
        """ Returns user's profile data with images """
        if self._profile is None:
            profile = self.get_object('me')
            profile['image'] = 'https://graph.facebook.com/me/picture?type=large&access_token=%s' % self.access_token
            profile['image_thumb'] = 'https://graph.facebook.com/me/picture?access_token=%s' % self.access_token
            self._profile = profile
        return self._profile
    
    def get_or_create_local_profile(self):
        """ Gets or creates the FacebookProfile (and local auth User) for the
        current access token """
        if not self.is_authenticated():
            raise FacebookNotAuthenticated("A valid access token is required.")
        
        has_user = True # has a User in our DB
        
        fb_profile = self.get_profile()
        try:
            return FacebookProfile.objects.get(facebook_id=fb_profile['id'])
        except FacebookProfile.DoesNotExist:
            try:
                user = User.objects.get(username=fb_profile['email'])
            except User.DoesNotExist:
                has_user = False
                     
        # User does not exist, create it
        if not has_user:
            user = User.objects.create_user(
                username=fb_profile['email'],
                email=fb_profile['email'],
                password=self._generate_fake_password(),
            )
            user.first_name = fb_profile['first_name']
            user.last_name = fb_profile['last_name']
            user.save()
        
        new_fb_profile = FacebookProfile.objects.create(
            user=user,
            facebook_id=fb_profile['id'],
            friend_ids=self.get_friend_ids_list(),
            access_token=self.access_token,
        )
        
        return new_fb_profile    

    def get_friend_ids_list(self):
        if not self.is_authenticated():
            raise FacebookNotAuthenticated("A valid access token is required.")
        
        friends = self.get_connections(self.get_profile()['id'], "friends")
        return [friend['id'] for friend in friends['data']]

    @classmethod
    def _generate_fake_password(cls):
        """ Returns a random fake password """
        import string
        from random import choice
        size = 9
        password = ''.join([choice(string.letters + string.digits) for i in range(size)])
        return password.lower()


    