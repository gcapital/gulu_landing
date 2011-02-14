""" Gulu photos module URLs """

__author__ = "Ben Homnick"
__version__ = "$Id: urls.py 570 2011-01-26 07:39:21Z gage $"

from django.conf.urls.defaults import *

urlpatterns = patterns('photos.views',
	# Add your URL patterns here
)

urlpatterns += patterns('photos.ajax',
	url(r'^ajax/update-best-photos/(?P<operation>add|remove)/(?P<restaurant_id>\d+)/(?P<photo_id>\d+)$', 'update_best_photos', name="ajax-photos-update-best-photos"),
	#url(r'^ajax/remove-from-photos/(?P<photo_type>restaurant|dish)/(?P<photo_id>\d+)$', 'remove_photo_from_photos', name="ajax-photos-remove-from-photos"),
	url(r'^ajax/upload_photo$', 'upload_photo', name="ajax-photos-upload-photo"),
)
