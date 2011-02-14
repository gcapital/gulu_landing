""" Gulu invite module views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 435 2010-12-22 08:58:57Z ben $"

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

from invite.forms import CreateInviteForm
from restaurant.models import Restaurant

@login_required
def create(request):
	
	if request.method == 'POST':
		form = CreateInviteForm(request.POST)
	
	else:
		form = CreateInviteForm()
	
	return render_to_response('invite_create.html', {
		'form': form,
		'restaurant': Restaurant.objects.get(pk=1),
	}, context_instance = RequestContext(request))
