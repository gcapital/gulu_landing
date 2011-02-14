""" Gulu dish module URLs """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: urls.py 568 2011-01-26 03:27:15Z ben $"

from django.conf.urls.defaults import *

#urlpatterns = patterns('dish.views',
#    url(r'restaurant-(?P<restaurant_id>\d+)/$', 'show_menu', name="dish-show-menu"),
#)

urlpatterns = patterns('dish.ajax',
    url(r'^ajax/show_menu$', 'show_menu', name="show-menu"),
	url(r'^ajax/search/(?P<restaurant_id>\d+)/$', 'search', name="dish-search"),
	url(r'^ajax/get-details/$', 'get_details', name="dish-get-details"),
)

