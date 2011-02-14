""" Gulu restaurant views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 593 2011-01-27 06:50:26Z ben $"

from django.template import RequestContext
from django.shortcuts import render_to_response

from actstream.models import actor_stream
from restaurant.models import RestaurantService
from wall.forms import WallPostForm

def profile(request, restaurant_id):
	""" Restaurant basic profile view """
	
	return render_to_response('restaurant_index.html', {
		'activities': actor_stream(request.content_object),
		'form': WallPostForm(owner=request.content_object),
		'services' : RestaurantService.objects.all(),
	}, context_instance=RequestContext(request))
