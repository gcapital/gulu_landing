""" Gulu mission module URLs """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: urls.py 403 2010-12-17 03:31:54Z de $"

from django.conf.urls.defaults import *

urlpatterns = patterns('mission.views',
	url(r'^$', 'index', name="mission_index"),
)
