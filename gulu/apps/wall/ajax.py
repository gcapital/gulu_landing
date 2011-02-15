""" Gulu wall module AJAX functions """

__author__ = "Jason Ke<u912538@gmail.com>"
__version__ = "$Id$"

import json

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.utils import simplejson
from django.utils.translation import ugettext as _

from actstream import action
from photos.models import Photo
from restaurant.models import Restaurant
from wall.forms import WallPostForm

@login_required
def post(request):
	""" Creates a new wall post """
	
	form = WallPostForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.poster = request.user
		post.save()
		
		# Attach the temp photo to this post
		photo_id = form.cleaned_data.get('photo_id')
		if photo_id:
			photo = Photo.objects.get(pk=photo_id)
			photo.attach(post)
			post.photo = photo
			post.save()
		
		# If this is a restaurant wall, the actor is actually the restaurant itself
		actor = post.poster
		if post.owner_content_type == ContentType.objects.get_for_model(Restaurant):
			actor = post.owner
		activity = action.send(actor, verb="posted on", action_object=post, target=post.owner)[0][1]
		
		response = {
			'status': 0,
			'html': activity.render(),
		}
	else:
		response = {
			'status': 1,
			'error': _(u"Could not create wall post.  Please try again later"),
		}
	
	return HttpResponse(simplejson.dumps(response), mimetype="application/json")
