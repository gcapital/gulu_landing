""" Gulu photos module AJAX views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: ajax.py 607 2011-01-27 08:29:59Z gage $"

import os
import json
import time

from django.http import HttpResponse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.template import RequestContext

from photos.models import Photo
from restaurant.models import Restaurant

def update_best_photos(request, operation, restaurant_id, photo_id):
	""" Adds/removes a RestaurantPhoto to/from a Restaurant's best photo set or a 
	DishPhoto to/from a Dish's best photo set.
	
	Example:
	
	{% url ajax-photos-update-best-photos "add" "restaurant" restaurant.id photo.id %}
	
	Args:
		operation:		Either 'add' or 'remove'
		photo_type:		Type of object, either 'restaurant' or 'dish'
		restaurant_id:	Restaurant id
		photo_id:		Photo id, if object_type=='restaurant' this is assumed
						to be a RestaurantPhoto, if object_type=='dish' this is 
						assumed to be a DishPhoto
	
	Returns:
		HTML an entire photo item with frame
		
	"""
	restaurant = Restaurant.objects.get(pk=restaurant_id)
	
	photo = Photo.objects.get(pk=photo_id)
	
	if operation == 'add':
		if len(list(restaurant.best_photos.all()))==9:
			return HttpResponse('full', mimetype="text/html")
		restaurant.best_photos.add(photo)
		
	elif operation == 'remove':
		restaurant.best_photos.remove(photo)

	request.content_object = restaurant

	photo_item_html = render_to_string('inc_photo_item.html',{
         'photo': photo,
    }, context_instance = RequestContext(request))
	
	return HttpResponse(photo_item_html, mimetype="text/html")

'''
def remove_photo_from_photos(request, photo_type, photo_id):
	""" remove dish/restaurant photo from photos.
		set is_showing to False
		
	Args:
		photo_type:		Either 'dish' or 'restaurant'
		photo_id:		photo id
		
	Returns:
		JSON encoded object:
		{
			'status':	1 if successful, 0 otherwise
		}
	
	"""
	
	if photo_type == 'restaurant':
		p = RestaurantPhoto.objects.get(pk=photo_id)
		r = p.restaurant
	elif photo_type == 'dish':
		p = DishPhoto.objects.get(pk=photo_id)
		r = p.dish.restaurant
	
	t = ContentType.objects.get_for_model(p)	
	
	if p.best_photos.all():
		bp = BestPhotos.objects.get(restaurant=r,photo_content_type=t, photo_id=photo_id)
		bp.delete()
	p.show_in_restaurant = False
	p.save()

		
	return HttpResponse(json.dumps({'status': 1}), mimetype="application/json")
'''

def upload_photo(request):
	""" Remotely uploads a photo and returns a JSON TempPhoto object
	
	GET Parameters:
		qqfile:		Name of the file being uploaded, if the browser supports XHR
					uploads this will apear in request.raw_post_data
		spec:		Name of the ImageSpec to proess this photo with.  Make sure
					the ImageSpec actually exists in photos.imagespecs otherwise
					bad things will happen.

	Returns:
		{
			'status':	1 if successful, 0 otherwise
			'id':		ID of the newly created TempPhoto object,
			'url':		URL to display the imagespec-processed photo requested,
			'message':	Error message, only if status==0,
		}
	"""		
	
	# TODO: IE case where XHR isn't supported, fall back to request.FILES
	
	def fail_upload(message):
		""" Returns a JSON response with fail status and error message """
		response = {
			'status': 0,
			'message': message,
		}
		return HttpResponse(json.dumps(response), mimetype="application/json")
	
	if request.method == 'POST':
		filename = request.GET.get('qqfile', None)
		if filename:
			# TODO: SimpleUploadedFile is the in-memory upload handler.  Is this
			# going to kill our server with large files?  
			
			# Create a unique filename
			file = SimpleUploadedFile(filename, request.raw_post_data)
			relative_path = "photos/%s_%s_%s" % (request.user.id, int(time.time()), filename)
			full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
			
			# Write the file to disk
			destination = open(full_path, 'wb+')
   			for chunk in file.chunks():
				destination.write(chunk)
			destination.close()
			
			# Create the photo object
			photo = Photo(image=relative_path, user=request.user)
			photo.save()

			# Try to use the spec provided
			spec = request.GET.get('spec', None)
			if not spec:
				return fail_upload("No imagespec specified.")
			if not hasattr(photo, spec):
				return fail_upload("Imagespec %s does not exist." % spec)

			response = {
				'status': 1,
				'id': photo.id,
				'url': getattr(photo, spec).url,
			}
			
			return HttpResponse(json.dumps(response), mimetype="application/json")
		else:
			return fail_upload("No file could be found.")
	
	return fail_upload("No file uploaded.  Please try again.")
