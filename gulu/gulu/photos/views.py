""" Gulu photo module views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 607 2011-01-27 08:29:59Z gage $"

from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from photos.models import Photo
from photos.forms import PhotoForm
from review.models import Review
from wall.models import WallPost

type_review = ContentType.objects.get_for_model(Review)
type_wall = ContentType.objects.get_for_model(WallPost)

def list(request, object_id):
	content_type = ContentType.objects.get_for_model(request.content_object)
	if content_type.model == 'restaurant':
		photos = Photo.objects.filter(
				Q(content_type=type_review) | 
				Q(content_type=type_wall)
			).filter(restaurant_id=object_id)
		
		restaurant = request.content_object
		
		return render_to_response("photos_%s_list.html" % content_type.model, {
			'photos': photos,
			'restaurant': restaurant,
		}, context_instance = RequestContext(request))
		
	else:
		photos = Photo.objects.filter(
				Q(content_type=type_review) | 
				Q(content_type=type_wall)
			).filter(user=request.content_object)
		
		return render_to_response("photos_%s_list.html" % content_type.model, {
			'photos': photos,
		}, context_instance = RequestContext(request))


@login_required
def change(request, content_type, object_id, photo_id = None, *args, **kwargs):
	content_object = content_type.get_object_for_this_type(pk=object_id)
	photo = None
	edit = False
	if photo_id:
		photo = get_object_or_404(Photo, pk=photo_id, content_type=content_type, 
								  object_id=object_id)
		edit = True
	
	if request.method == 'POST':
		form = PhotoForm(data=request.POST, files=request.FILES, instance=photo, 
						 content_object=content_object,  edit=edit)
		
		if form.is_valid():
			new_photo = form.save(commit=False)
			new_photo.content_type = content_type
			new_photo.object_id = object_id
			new_photo.user = request.user
			new_photo.save()
			return HttpResponseRedirect(new_photo.get_absolute_url())
	
	else:
		form = PhotoForm(content_object=content_object, instance=photo, edit=edit)

	return render_to_response("photos_change.html", {
		'photo': photo,
		'form': form,
	}, context_instance = RequestContext(request))


def view(request, object_id, photo_id):
	photo = get_object_or_404(Photo, pk=photo_id)
	object = photo.content_object
	
	return render_to_response("photos_view.html", {
		'photo': photo,
		'object': object,
	}, context_instance = RequestContext(request))