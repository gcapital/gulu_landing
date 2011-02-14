""" Gulu user profile module views """

__author__ = "gage <gage.tseng@geniecapital.com>"
__version__ = "$Id: views.py 580 2011-01-27 03:45:09Z ben $"

from django.template import RequestContext
from django.shortcuts import render_to_response

from actstream.models import actor_stream, Follow
from wall.forms import WallPostForm

def profile(request, user_id):
	""" User profile page """
	
	# User is viewing their own wall
	if request.content_object == request.user:
		activities = Follow.objects.stream_for_user(request.user)
	# User is viewing someone else's wall
	else:
		activities = actor_stream(request.content_object)
		
	return render_to_response("mygulu_profile_index.html", {
		'activities': activities,
		'form': WallPostForm(owner=request.content_object),
	}, context_instance=RequestContext(request))
