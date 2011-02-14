""" Gulu like views """


import json
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext

from like.models import Like

@login_required
def process(request, action, content_type_id, object_id, redirect_field='next'):
	"""
	Processes a like or dislike request.
	
	For ajax requests returns HTTP 200 is successful, HTTP 400 otherwise.
	For other requests redirects to whatever is in the redirect_field.
	"""
	
	content_type = get_object_or_404(ContentType, id=content_type_id)
	content_object = get_object_or_404(content_type.model_class(), pk=object_id)
	
	if action == "like":
		Like.objects.like(request.user, content_object)
	else:
		Like.objects.unlike(request.user, content_object)
	
	if request.GET.get(redirect_field) and not request.is_ajax():
		return HttpResponseRedirect(request.GET[redirect_field])
	
	all_like_items = Like.objects.filter(content_type=content_type_id, object_id=object_id).exclude(user=request.user)
	count = all_like_items.count()
	
	if action == 'like':
		count += 1

	if count > 3:
		like_items = all_like_items[:3]
		others = count-3
	else:
		like_items = all_like_items
		others = 0
	
	like_info_html = render_to_string('inc_like_info.html',
			{
				'like_type': action,
				'user': request.user,
				'like_items': like_items,
				'others': others,
				'like_count': count,
			},
			context_instance=RequestContext(request))
	
	if action == "like":
		return HttpResponse(json.dumps({'type':'1', 'like_info':like_info_html}), mimetype="application/json")
	else:
		return HttpResponse(json.dumps({'type':'0', 'like_info':like_info_html}), mimetype="application/json")
	