from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, OAuthAuthentication
from piston.doc import documentation_view
from piston.emitters import Emitter, DjangoEmitter


from api.handlers import *
from api.event_handler import *
from api.user_handler import *
from api.wall_comment_handler import *
from api.dummy_handler import *
 

auth = HttpBasicAuthentication(realm="Test Realm")

"""api.handlers"""
dishes_rid = Resource(handler=get_dish_by_rid)
dishes_term = Resource(get_dish_by_term)#fake
dish_rid_term_type = Resource(get_dish_by_rid_term_type)#fake
reviews_uid = Resource(handler=get_review_by_uid)
reviews_rid = Resource(handler=get_review_by_rid)
reviews_new = Resource(handler=create_review)#fake
deals_rid = Resource(handler=get_deal_by_rid)
deals_nearby = Resource(handler=get_deal_nearby)
restaurants_nearby = Resource(handler=get_restaurant_nearby)
restaurant_rid = Resource(handler=get_restaurant_info)
restaurant_term_dish = Resource(get_restaurant_search_by_term_and_dishname)#fake
restaurant_near_term = Resource(get_restaurant_search)#fake
photo_new = Resource(handler=create_photo)
wall_uid = Resource(handler=get_wall_post_by_uid)#new
wall_new = Resource(handler=create_wall_post)#fake
wall_comment_new = Resource(handler=create_wall_post_comment)#fake
wall_comment_pid = Resource(handler=get_wall_comment_by_postid)#fake
wall_delete = Resource(handler=delete_wall_post)#fake
wall_comment_delete = Resource(handler=delete_wall_post_comment)#fake



"""api.event_handler"""
events_uid = Resource(handler=get_event_by_uid)
event_new = Resource(handler=create_event)
event_update = Resource(handler=update_event)
"""api.user_handler"""
user_uid = Resource(handler=get_user_info)
check_username = Resource(handler=signup_checkusername)
check_email = Resource(handler=signup_checkemail)
signup = Resource(handler=signup)
signin = Resource(handler=signin)
upload_user_info = Resource(handler=upload_user_info)
"""api.facebook_api"""





"""Default { 'emitter_format': 'json' }"""
urlpatterns = patterns('',
    url(r'^get_dish_by_rid/', dishes_rid),    
    url(r'^get_dish_by_term', dishes_term),#fake
    url(r'^get_dish_by_rid_term_type', dish_rid_term_type),#fake

    url(r'^get_review_by_uid', reviews_uid),
    url(r'^get_review_by_rid', reviews_rid),    
    url(r'^create_review', reviews_new),#fake

    url(r'^get_deal_by_rid', deals_rid),
    url(r'^get_deal_nearby', deals_nearby),
    
    url(r'^get_restaurant_nearby', restaurants_nearby),
    url(r'^get_restaurant_info', restaurant_rid),    
    url(r'^get_restaurant_search_by_term_and_dishname', restaurant_term_dish),#fake
    url(r'^get_restaurant_search/', restaurant_near_term),#fake

    url(r'^create_photo', photo_new),
    
    url(r'^get_wall_post_by_uid', wall_uid),#fake
    url(r'^create_wall_post/', wall_new),#fake
    url(r'^create_wall_post_comment', wall_comment_new),#fake
    url(r'^get_wall_comment_by_postid', wall_comment_pid),#fake
    url(r'^delete_wall_post/', wall_delete),#fake
    url(r'^delete_wall_post_comment', wall_comment_delete),#fake
        
    url(r'^get_event_by_uid', events_uid),
    url(r'^create_event', event_new),
    url(r'^update_event', event_update),
    
    url(r'^get_user_info', user_uid),
    url(r'^signup_checkusername', check_username),
    url(r'^signup_checkemail', check_email),
    url(r'^signin', signin),
    url(r'^signup', signup),
    url(r'^upload_user_info', upload_user_info),
    
    # automated documentation
    url(r'^$', documentation_view),
)

"""Authentication"""
urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)
"""Oauth Consumer"""
urlpatterns += patterns('',
    url(r'^oauth_ask_approve/(?P<site_name>.+)/$', 'api.oauth_consumer.oauth_ask_approve'),
    url(r'^oauth_handle_token/(?P<site_name>.+)/$', 'api.oauth_consumer.oauth_handle_token'),
)

"""Twitter"""
urlpatterns += patterns(
    'api.twitter_api',
    url(r'^tweet_a_message/$', 'tweet_a_message'),
        
)

"""Facebook"""
urlpatterns += patterns('api.facebook_api',
    url(r'^sync_fb', 'oauth_facebook_request'),
    url(r'^oauth_facebook_access', 'oauth_facebook_access'),
    url(r'^cancel_facebook_account', 'facebook_cancel'),  
    url(r'^facebook_postwall', 'facebook_postwall'),
        
)

"""Dummy"""
urlpatterns += patterns('api.dummy_handler',
    url(r'^restaurant_dummy', 'restaurant_dummy'),
    url(r'^doc', 'doc_dummy'),
        
)