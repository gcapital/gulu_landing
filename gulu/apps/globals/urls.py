""" Gulu dish module URLs """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: urls.py 559 2011-01-24 04:43:59Z jason $"

from django.conf.urls.defaults import *

urlpatterns = patterns('globals.views',
    url(r'^$', 'home', name="home_index"),
)
#urlpatterns = patterns('restaurant.ajax',
#    url(r'^ajax/search-restaurants$', 'search_restaurants', name="ajax-restaurant-search-restaurants"),
#    url(r'^ajax/get-restaurant-details$', 'get_restaurant_details', name="ajax-restaurant-get-restaurant-details"),
#
#)