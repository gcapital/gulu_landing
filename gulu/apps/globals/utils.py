""" Gulu global utility functions """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: utils.py 539 2011-01-12 06:10:52Z ben $"

from django.core.urlresolvers import reverse

def slugreverse(slug_object, viewname, urlconf=None, args=None, kwargs=None, current_app=None):
	""" Reverses a view to a slug-based URL 
	
	Args:
		slug_object:	Any object with a 'slug' attribute, if slug is not
						None, the first two parameters of the reversed URL will
						be replaced with this slug.
		
		For other arguments see the django.core.urlresolvers.reverse
	
	Returns:
		A slug-based URL.
	"""

	url = reverse(viewname, urlconf, args, kwargs, current_app)
	if hasattr(slug_object, 'slug') and slug_object.slug:
		return "/%s/%s" % (slug_object.slug, "/".join(url.split("/")[3:]))
	return url



