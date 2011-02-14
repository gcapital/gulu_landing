""" Gulu invite module URLs """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: urls.py 388 2010-12-16 06:59:01Z ben $"

from django.conf.urls.defaults import *

urlpatterns = patterns('invite.views',
	url(r'^$', 'create', name="invite_create"),
)

urlpatterns += patterns('invite.ajax',
	url(r'^ajax/get-invite-choices', 'get_invite_choices', name="ajax-invite-get-invite-choices"),
)