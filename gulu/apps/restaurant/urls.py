""" Gulu restaurant module URLs """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: urls.py 593 2011-01-27 06:50:26Z ben $"

from django.conf.urls.defaults import *
from django.contrib.contenttypes.models import ContentType

urlpatterns = patterns('',
	url(r'^(?P<restaurant_id>\d+)/$', 'restaurant.views.profile', name="restaurant-profile"),

	url(r'^(?P<restaurant_id>\d+)/reviews/$', 'review.views.view_index', name="restaurant-reviews"),
	url(r'^(?P<restaurant_id>\d+)/reviews/(?P<review_id>\d+)/$', 'review.views.view_detail', name="restaurant-view-review"),

	url(r'^(?P<object_id>\d+)/photos/$', 'photos.views.list', name="photos-restaurant-list"),
	url(r'^(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/$', 'photos.views.view', name="photos-restaurant-view"),
	url(r'^(?P<object_id>\d+)/photos/add/$', 'photos.views.change', name="photos-restaurant-add"),
	url(r'^(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/edit/$', 'photos.views.change', name="photos-restaurant-edit"),

	url(r'^(?P<restaurant_id>\d+)/menu/$', 'dish.views.menu', name="restaurant-menu"),
	url(r'^(?P<restaurant_id>\d+)/menu/(?P<dish_id>\d+)/$', 'dish.views.view_dish', name="restaurant-view-dish"),
	url(r'^(?P<restaurant_id>\d+)/menu/add/$', 'dish.views.add_dish', name="restaurant-add-dish"),
	url(r'^(?P<restaurant_id>\d+)/menu/(?P<dish_id>\d+)/edit/$', 'dish.views.edit_dish', name="restaurant-edit-dish"),
	
#	url(r'^(?P<restaurant_id>\d+)/menu/(?P<object_id>\d+)/photos/$', 'photos.views.list', {'content_type': dish_type}, name="photos-dish-list"),
#	url(r'^(?P<restaurant_id>\d+)/menu/(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/$', 'photos.views.view', {'content_type': dish_type}, name="photos-dish-view"),
#	url(r'^(?P<restaurant_id>\d+)/menu/(?P<object_id>\d+)/photos/add/$', 'photos.views.change', {'content_type': dish_type}, name="photos-dish-add"),
#	url(r'^(?P<restaurant_id>\d+)/menu/(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/edit/$', 'photos.views.change', {'content_type': dish_type}, name="photos-dish-edit"),

	url(r'^(?P<restaurant_id>\d+)/blog/$', 'blog.views.restaurant_posts', name="restaurant-posts"),
	url(r'^(?P<restaurant_id>\d+)/blog/(?P<post_id>\d+)/$', 'blog.views.restaurant_view_post', name="restaurant-view-post"),
	url(r'^(?P<restaurant_id>\d+)/blog/add/$', 'blog.views.restaurant_add_post', name="restaurant-add-post"),
	url(r'^(?P<restaurant_id>\d+)/blog/(?P<post_id>\d+)/edit/$', 'blog.views.restaurant_edit_post', name="restaurant-edit-post"),

	url(r'^(?P<restaurant_id>\d+)/other-locations/$', 'locations.views.restaurant_other_locations', name="restaurant-other-locations"),
	url(r'^(?P<restaurant_id>\d+)/other-locations/add/$', 'locations.views.restaurant_add_other_location', name="restaurant-add-other-location"),
	url(r'^(?P<restaurant_id>\d+)/other-locations/handle/(?P<invitation_id>\d+)/(?P<action>accept|decline)/$', 'locations.views.restaurant_handle_invitation', name="restaurant-handle-invitation"),

	url(r'^(?P<restaurant_id>\d+)/deals/$', 'deal.views.deals', name="deal-deals"),
	url(r'^(?P<restaurant_id>\d+)/deals/(?P<deal_id>\d+)/$', 'deal.views.view_deal', name="deal-view-deal"),
	url(r'^(?P<restaurant_id>\d+)/deals/add/$', 'deal.views.add_deal', name="deal-add-deal"),
	url(r'^(?P<restaurant_id>\d+)/deals/(?P<deal_id>\d+)/edit/$', 'deal.views.edit_deal', name="deal-edit-deal"),
	
	url(r'^(?P<restaurant_id>\d+)/chefs/$', 'chef.views.view_chef', name="restaurant-chef"),
	url(r'^(?P<restaurant_id>\d+)/chefs/add/$', 'chef.views.add_chef', name="restaurant-add-chef"),

)
#	url(r'(?P<restaurant_id>\w+)/videos', 'videos', name="restaurant-videos"),
#	url(r'(?P<restaurant_id>\w+)/menu', 'menu', name="restaurant-menu"),
#	url(r'(?P<restaurant_id>\w+)/blog', 'blog', name="restaurant-blog"),
#	url(r'(?P<restaurant_id>\w+)/other-location', 'other_locations', name="restaurant-other-locations"),
#	url(r'(?P<restaurant_id>\w+)/missions', 'missions', name="restaurant-missions"),
#	url(r'(?P<restaurant_id>\w+)/deals', 'deals.views.show_deals', name="restaurant-deals"),


urlpatterns += patterns('restaurant.ajax',
	url(r'^ajax/search-restaurants$', 'search_restaurants', name="ajax-restaurant-search-restaurants"),
	url(r'^ajax/get-restaurant-details$', 'get_restaurant_details', name="ajax-restaurant-get-restaurant-details"),
)
