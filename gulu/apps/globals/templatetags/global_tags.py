""" Gulu global template tags 

Contains various utility tags used throughout the Gulu project.
"""

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: global_tags.py 408 2010-12-20 06:51:41Z gage $"

import re
import random

from django import template
from django.template import Node, NodeList, Template, Context, Variable
from django.core.urlresolvers import reverse

register = template.Library()
# Regex for token keyword arguments
kwarg_re = re.compile(r"(?:(\w+)=)?(.+)")

class SlugURLNode(Node):
	def __init__(self, slug_object, view_name, args, kwargs):
		self.slug_object = template.Variable(slug_object)
		self.view_name = view_name
		self.args = args
		self.kwargs = kwargs

	def render(self, context):
		args = [arg.resolve(context) for arg in self.args]
		kwargs = dict([(smart_str(k,'ascii'), v.resolve(context))
					   for k, v in self.kwargs.items()])

		url = reverse(self.view_name, args=args, kwargs=kwargs, current_app=context.current_app)
		
		slug = self.slug_object.resolve(context).slug
		if slug:
			url = "/%s/%s" % (slug, "/".join(url.split("/")[3:]))
		
		return url

def slugurl(parser, token):
	""" Returns a slug-based URL for objects that have a 'slug' attribute (currently 
	restaurants and user_profiles).  
	
	Example:
		{% slugurl slug_object view_name arg1 arg2 %}
		
	The first argument is the object which contains the slug attribute, followed
	by the view name and any view arguments.
	
	For instance, if restaurant.slug = 'dozo',
	
	{% slugurl restaurant restaurant-photos %}
	
	will return /dozo/photos/.  If restaurant.slug = None, the same call will 
	return /restaurant/3/photos/.
	"""
	
	bits = token.split_contents()
	if len(bits) < 3:
		raise TemplateSyntaxError("'%s' takes at least two arguments (restaurant object, path to a view)" % bits[0])
		
	slug_object = bits[1]
	viewname = bits[2]
	args = []
	kwargs = {}
	bits = bits[3:]

	# Now all the bits are parsed into new format,
	# process them as template vars
	if len(bits):
		for bit in bits:
			match = kwarg_re.match(bit)
			if not match:
				raise TemplateSyntaxError("Malformed arguments to url tag")
			name, value = match.groups()
			if name:
				kwargs[name] = parser.compile_filter(value)
			else:
				args.append(parser.compile_filter(value))

	return SlugURLNode(slug_object, viewname, args, kwargs)

slugurl = register.tag(slugurl)



class RandomClassNode(Node):
	def __init__(self, args):
		self.args = args
	
	def render(self, context):
		classes = self.args
		return classes[int(random.random()*len(classes))]

def get_random(parser, token):
	bits = token.split_contents()
	bits = bits[1:]
	args = []
	if len(bits):
		for bit in bits:
			args.append(parser.compile_filter(bit))
	return RandomClassNode(args)
get_random = register.tag(get_random)
