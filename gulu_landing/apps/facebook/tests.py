""" Facebook tests """

import urllib

from django.db import connection
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.simple import DjangoTestSuiteRunner

from nose.tools import with_setup

from facebook.facebook_api import FacebookAPI
from facebook.models import FacebookProfile

class FacebookTestEnvironment(object):

    def __init__(self):
        self._auth_token = None
        self.u1 = None
        self.u2 = None
        self.u3 = None
    
    def _get_auth_token(self):
        if not self._auth_token:
            auth_url = "https://graph.facebook.com/oauth/access_token?client_id=%s&" \
                "client_secret=%s&grant_type=client_credentials" % \
                (settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
            self._auth_token = urllib.urlopen(auth_url).read()[13:]
        return self._auth_token
    
    def _create_test_user(self):
        fb = FacebookAPI(access_token=self._auth_token)
        user_args = {
            'installed': "true",
            'permissions': "offline_access,email",
        }
        user_url = "%s/accounts/test-users" % settings.FACEBOOK_APP_ID
        return fb.request(user_url, user_args, {})            
    
    def _make_friends(self, u1, u2):
        for pair in [(u1, u2), (u2, u1)]:
            fb = FacebookAPI(access_token=pair[0]['access_token'])
            fb.request("%s/friends/%s" % (pair[0]['id'], pair[1]['id']), post_args={})            
        return True
    
    def _delete_test_user(self, uid):
        fb = FacebookAPI(access_token=self._auth_token)
        fb.delete_object(uid)


test_env = FacebookTestEnvironment()
   

class FacebookTest(TestCase):
    
    @classmethod
    def setupClass(cls):
        print "\n******\nSetting up facebook environment..."
        print "Getting auth token..."
        test_env._get_auth_token()
        print "Creating three users..."
        test_env.u1 = test_env._create_test_user()
        test_env.u2 = test_env._create_test_user()
        test_env.u3 = test_env._create_test_user()
        print "Friending users..."
        test_env._make_friends(test_env.u1, test_env.u2)
        test_env._make_friends(test_env.u1, test_env.u3)
        print "Done!\n******\n"
    
    @classmethod
    def teardownClass(cls):
        print "\n******\nDeleting three users..."
        test_env._delete_test_user(test_env.u1['id'])
        test_env._delete_test_user(test_env.u2['id'])
        test_env._delete_test_user(test_env.u3['id'])
        print "Done!\n******\n"
    

class APITest(FacebookTest):
    """ tests facebook_api.py """
    def test_get_profile(self):
        api = FacebookAPI(access_token=test_env.u1['access_token'])
        self.assertEqual(api.get_profile()['id'], test_env.u1['id'])

    def test_is_authenticated(self):
        api = FacebookAPI(access_token=test_env.u1['access_token'])
        self.assertTrue(api.is_authenticated())
        
        api2 = FacebookAPI()
        self.assertFalse(api2.is_authenticated())
    
    def test_get_friends(self):
        api = FacebookAPI(access_token=test_env.u1['access_token'])
        u1_friends = api.get_connections(test_env.u1['id'], 'friends')
        self.assertEqual(u1_friends['data'][0]['id'], test_env.u2['id'])
    
    def test_get_or_create_local_profile(self):
        # TODO: verify connection.queries is accurate with MongoDB, looks
        # like only finds are recorded
        old_debug = settings.DEBUG
        settings.DEBUG = True
        connection.queries = []
        
        # no local user or fb profile
        api = FacebookAPI(access_token=test_env.u1['access_token'])
        remote_profile = api.get_profile()
        p1 = api.get_or_create_local_profile()
        self.assertEquals(p1, 
            FacebookProfile.objects.get(facebook_id=test_env.u1['id']))
        self.assertEquals(p1.user,
            User.objects.get(username=remote_profile['email']))        
                
        # local user, no fb profile
        api2 = FacebookAPI(access_token=test_env.u2['access_token'])
        remote_profile2 = api2.get_profile()
        u2 = User.objects.create_user(username=remote_profile2['email'],
            email=remote_profile2['email'], password="taters")
        p2 = api2.get_or_create_local_profile()
        self.assertEquals(p2,
            FacebookProfile.objects.get(facebook_id=test_env.u2['id']))
        self.assertEquals(p2.user, u2)
        
        # local user, local fb profile
        p2 = api2.get_or_create_local_profile()
        self.assertEquals(p2,
            FacebookProfile.objects.get(facebook_id=test_env.u2['id']))
        self.assertEquals(FacebookProfile.objects.all().count(), 2)
        self.assertEquals(User.objects.all().count(), 3) # Add one for AnonymousUser
     
        settings.DEBUG = old_debug
    
    def test_get_friend_ids_list(self): 
        api = FacebookAPI(access_token=test_env.u1['access_token'])
        
        self.assertEquals(set([test_env.u2['id'], test_env.u3['id']]),
            set(api.get_friend_ids_list()))




