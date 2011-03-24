""" gulu-landing global URLs """

__author__ = "Ben Homnick <bhomnick@gmail.com>"

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'landing.views.index', name="landing-index"),
	
	
	(r'^facebook/', include('facebook.urls')),
	
    # Static media - dev only
	(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
