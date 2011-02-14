""" Gulu globals module views """

import json
import logging

from django import http
from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _
from django.utils.translation.trans_real import parse_accept_lang_header

from globals.forms import CreateNewsletterForm

from mailsnake.mailsnake import MailSnake

logger = logging.getLogger("gulu")

def redirect404(request):
	return redirect("globals-home")

def home(request):	  
	""" Temp landing page """
	
	if request.method == 'POST':
		form = CreateNewsletterForm(request.POST)
		if form.is_valid():
			ms = MailSnake(settings.MAILSNAKE_API_KEY)
			post = form.save(commit=False)
			subscribed = ms.listSubscribe(id='279790dbdc', email_address=post.email, 
				double_optin=False, merge_vars=post.username)

			if subscribed == True or subscribed['code'] == 214:
				post.save()
			else:
				form._errors['username'] = form.error_class([_(u"Could not subscribe.  Please try again later.")])
				logger.error("Subscription failed for %s: %s" % (post.email, subscribed['error']))
	else:
		form = CreateNewsletterForm()

	return render_to_response("index.html", {
		'form': form,
	}, context_instance = RequestContext(request))
