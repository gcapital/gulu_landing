""" Gulu todo module views """

__author__ = "Jason Ke <jason.ke@geniecapital.com>"
__version__ = "$Id: views.py 1 2011-01-26 07:50:47Z jason $"

from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from user_profiles.models import UserProfile

@login_required
def list(request, user_id):
    """ User todo list view """
    
    user_profile = get_object_or_404(UserProfile, pk=user_id)
#    post = get_object_or_404(UserPost, owner=user_profile, pk=post_id)
    
    return render_to_response('todo_list.html', {
        'user_profile': user_profile,
    }, context_instance = RequestContext(request))
    