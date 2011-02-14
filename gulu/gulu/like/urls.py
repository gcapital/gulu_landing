""" Gulu like module URLs """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: urls.py 388 2010-12-16 06:59:01Z ben $"

from django.conf.urls.defaults import *

urlpatterns = patterns('like.views',
	url(r'^(?P<action>like|unlike)/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', 'process', name="like_process"),
)
