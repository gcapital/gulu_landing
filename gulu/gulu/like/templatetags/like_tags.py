""" Gulu like template tags """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id:$"

from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from like.models import Like

register = template.Library()

def get_kwargs(content_object):
	kwargs = {
		'content_type_id': ContentType.objects.get_for_model(content_object).id,
		'object_id': content_object.pk,
    }
	return kwargs

@register.simple_tag
def get_like_process_url(like, content_object):
	"""
	Gets URL to like an object:
	{% get_like_process_url "like" obj %}
	or dislike an object:
	{% get_like_process_url "dislike" obj %}
	"""
	kwargs = get_kwargs(content_object)
	kwargs["action"] = like
	return reverse('like.views.process', kwargs=kwargs)

@register.inclusion_tag('inc_like_btn.html', takes_context = True)
def like(context, content_object):
	user = context['request'].user
	if not user.is_anonymous():
		if Like.objects.does_like(user, content_object):
			like_type = 'like'
		else:
			like_type = 'unlike'

		content_type_id = ContentType.objects.get_for_model(content_object).id
		object_id = content_object.pk
		all_like_items = Like.objects.filter(content_type=content_type_id, object_id=object_id).exclude(user=user)
		count = all_like_items.count()
		
		if like_type == 'like':
			count += 1
	
		if count > 3:
			like_items = all_like_items[:3]
			others = count-3
		else:
			like_items = all_like_items
			others = 0
	
		return {
			'obj': content_object,
			'content_type_id' : content_type_id,
			'object_id' : object_id,
			'like_type': like_type,
			'user': user,
			'like_items': like_items,
			'others': others,
			'like_count': count,
		}
	else:
		like_type = 'unlike'
		content_type_id = ContentType.objects.get_for_model(content_object).id
		object_id = content_object.pk
		return {
			'obj': content_object,
			'content_type_id' : content_type_id,
			'object_id' : object_id,
			'like_type': like_type,
		}