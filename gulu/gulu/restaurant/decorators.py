""" Gulu restaurant module decorators """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: decorators.py 388 2010-12-16 06:59:01Z ben $"

from django.utils.functional import wraps
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404

from restaurant.models import Restaurant

def restaurant_view_wrapper(view):
	""" Converts a restaurant URL to a restaurant object
	
	Restaurant URLs can take either IDs or slugs to identify a restaurant.  This
	wrapper checks if a slug exists, and if so redirects to the URL containing the
	slug.  For instance,
	
	/restaurant/2/reviews -> /chi-ban-ramen/reviews
	/restaurant/chi-ban-ramen -> /chi-ban-ramen
	
	Views will receive a Restaurant object instead of ID to save on queries.
	"""
	
	@wraps(view)
	def _process(request, restaurant_id, *args, **kwargs):
		
		request.urlconf = 'gulu.urls'
		
		if restaurant_id.isdigit():
			r = get_object_or_404(Restaurant, pk=restaurant_id)
		else:
			r = get_object_or_404(Restaurant, slug=restaurant_id)

		path = request.path.split('/')
		if r.slug and (r.slug != restaurant_id or path[1] == 'restaurant'):
			return HttpResponsePermanentRedirect("/%s/%s" % (r.slug, '/'.join(path[3:])))

		return view(request, r, *args, **kwargs)
	return _process
