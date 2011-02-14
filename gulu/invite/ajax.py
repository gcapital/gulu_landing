""" Gulu invite module AJAX functions """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: ajax.py 576 2011-01-26 08:16:00Z ben $"

import json
from django.http import HttpResponse
from django.db.models import Q
#from user_profiles.models import UserFollower

def get_invite_choices(request):
	""" Returns a JSON encoded list of possible invite choices.
	
	Data is returned in the form:
	
	[
		{
			'id': <user/follower id>,
			'type': <{user|follower}>,
			'name': <user's full name>,
			'has_sms': <true|false>,
			'has_email': <true|false>,
			'pic': <img URL>,
		},
	]
	"""
	
	query = request.GET.get('q', None)
	
	data = []
	#followers = UserFollower.objects.filter(user=request.user)
	
	if query:
		followers = followers.filter(
			Q(follower__first_name__icontains=query) | Q(follower__last_name__icontains=query)
		)
	
	for follower in followers:
		f = follower.follower
		data.append({
			'id': f.pk,
			'type': 'follower',
			'name': f.get_full_name(),
			'has_sms': True,
			'has_email': True,
			'pic': f.main_profile_pic.image40x40.url,
		})
	
	return HttpResponse(json.dumps(data), mimetype="application/json")