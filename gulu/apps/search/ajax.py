""" Gulu search module AJAX functions """

__author__ = "Jason Ke<u912538@gmail.com>"
__version__ = "$Id$"

import json
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.translation import ugettext as _
from restaurant.models import Restaurant
from haystack.query import SearchQuerySet

def basic_search(query):
	""" Perform a basic search 
	
	Returns a SearchQuerySet
	"""

	raw_query = "*%s*" % "*_*".join(query.strip().split(" "))
	sqs = SearchQuerySet()
	return sqs.filter(content__icontains=sqs.query.clean(query))

def wildcard_search(query):
	""" Performs a wildcard search
	
	Returns a SearchQuerySet
	"""
	
	raw_query = "*%s*" % "*_*".join(query.strip().split(" "))
	print raw_query
	sqs = SearchQuerySet()
	return sqs.auto_query("spic")