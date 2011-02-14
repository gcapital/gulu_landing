""" Gulu user profiles module URLs """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: urls.py 607 2011-01-27 08:29:59Z gage $"

from django.conf.urls.defaults import *
from django.contrib.contenttypes.models import ContentType

from user_profiles.models import UserProfile

urlpatterns = patterns('',
	
	url(r'^(?P<user_id>\d+)/$', 'user_profiles.views.profile', name="user-profile"),
	
	url(r'^(?P<user_id>\d+)/todo/$', 'todo.views.list', name="todo-list"),
	
	url(r'^(?P<user_id>\d+)/blog/$', 'blog.views.user_posts', name="user-posts"),
	url(r'^(?P<user_id>\d+)/blog/(?P<post_id>\d+)/$', 'blog.views.user_view_post', name="user-view-post"),
	url(r'^(?P<user_id>\d+)/blog/add/$', 'blog.views.user_add_post', name="user-add-post"),
	url(r'^(?P<user_id>\d+)/blog/(?P<post_id>\d+)/edit/$', 'blog.views.user_edit_post', name="user-edit-post"),
	
	url(r'^(?P<object_id>\d+)/photos/$', 'photos.views.list', name="photos-userprofile-list"),
	url(r'^(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/$', 'photos.views.view', name="photos-userprofile-view"),
	url(r'^(?P<object_id>\d+)/photos/add/$', 'photos.views.change', name="photos-userprofile-add"),
	url(r'^(?P<object_id>\d+)/photos/(?P<photo_id>\d+)/edit/$', 'photos.views.change', name="photos-userprofile-edit"),
	
	url(r'^(?P<user_id>\d+)/reviews/$', 'review.views.user_view_index', name="user-review-index"),
	url(r'^(?P<user_id>\d+)/reviews/(?P<review_id>\d+)/$', 'review.views.user_view_detail', name="user-view-review-post"),
	#url(r'^(?P<username>\w+)/$', 'user_profiles.views.profile_index', name="user-profiles-test"),
	
	url(r'^(?P<user_id>\d+)/rankings/$', 'recommend.views.index', name="user-rankings"),
)