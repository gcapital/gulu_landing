""" Gulu global middleware classes """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: middleware.py 559 2011-01-24 04:43:59Z jason $"

from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _

from user_profiles.models import UserProfile
from restaurant.models import Restaurant
from globals.views import handler403

class Django403Middleware(object):
    """
    Replaces vanilla django.http.HttpResponseForbidden() responses
    with a rendering of 403.html
    """
    def process_response(self, request, response):
        # If the response object is a vanilla 403 constructed with
        # django.http.HttpResponseForbidden() then call our custom 403
        # view function
        if isinstance(response, HttpResponseForbidden) and \
               set(dir(response)) == set(dir(HttpResponseForbidden())):
            #if settings.DEBUG:
            #    raise PermissionDenied(_(
            #        "You don't have permission to access %s on this server.") % request.path)
            return handler403(request)
        return response
        

URL_MODEL_MAPPINGS = {
	'restaurant': Restaurant,
	'users': UserProfile,
}

URL_BASE_TEMPLATE_MAPPINGS = {
	'restaurant': "restaurant_base.html",
	'users': "mygulu_base.html",
}

URL_ESCAPE_KEYWORDS = [
    'ajax',
]

class SlugURLMiddleware(object):
	""" Middleware class for handling URLs with dynamic first parameters based
	on models' slug fields.
	"""
	
	def process_request(self, request):
		
		request.content_object = None
		request.base_template = None
		path = request.path.split('/')
		
		# Ignore root URL
		if not path[1]:
			return
		
		# If we're using a non-slug URL like "/restaurant/3/" and the object
		# actually has a valid slug field, we need to do a permanent redirect
		# to the slug-based URL
		if URL_MODEL_MAPPINGS.has_key(path[1]):
			
			# Ignore URLs with no second component
			try:
				if path[2] == "" or path[2] in URL_ESCAPE_KEYWORDS:
					return
			except IndexError:
				return
			
			obj = URL_MODEL_MAPPINGS[path[1]].objects.get(pk=path[2])
			request.content_object = obj
			request.base_template = URL_BASE_TEMPLATE_MAPPINGS[path[1]]
			if obj.slug:
				return HttpResponsePermanentRedirect("/%s/%s" % (obj.slug, "/".join(path[3:])))
		
		# If we are using a valid slug-based URL change request.path_info back into
		# the non-slug URL for django to play with.
		for prefix, model in URL_MODEL_MAPPINGS.iteritems():
			try:
				obj = model.objects.get(slug=path[1])
				request.content_object = obj
				request.base_template = URL_BASE_TEMPLATE_MAPPINGS[prefix]
				request.path_info = "/%s/%s/%s" % (prefix, obj.id, "/".join(path[2:]))
				
				# Common middleware won't append a slash in this case so we need
				# to manually add it.
				if settings.APPEND_SLASH and not request.path.endswith('/'):
					return HttpResponsePermanentRedirect("%s/" % request.path)
				return
				
			except model.DoesNotExist:
				pass

		return
