""" Gulu invite module AJAX functions """
__author__ = "Jason Ke<u912538@gmail.com>"
__version__ = "$Id$"

import json
from datetime import datetime
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.translation import ugettext as _
from review.models import Review
from restaurant.models import Restaurant
from dish.models import Dish
from user_profiles.models import UserProfile
from review.forms import CreateReviewForm
from photos.models import Photo
from actstream import action

def review_display_added_post(request):
	"""content = request.POST.get('content',None)
	restaurant_id = request.POST.get('restaurant_id',None)
	user_id = request.POST.get('user_id',None)
	dish_id = request.POST.get('dish_id',None)
	total_comment = 0
	
	restaurant = Restaurant.objects.get(pk=restaurant_id)
	user = UserProfile.objects.get(pk=user_id)
	dish = Dish.objects.get(pk=dish_id)
	
	review = Review(restaurant=restaurant,user=user, dish=dish, content=content, total_comment=total_comment)
	review.save()"""

	form = CreateReviewForm(request.POST)
	photo_id = request.POST.get('photo_id', None)

	if form.is_valid():
		review = form.save()
		# send the activity stream action signal
		action.send(request.user, verb="posted a review", target=review)
		if photo_id:
			tmp_photo = Photo.objects.get(pk=photo_id)
			tmp_photo.content_type = ContentType.objects.get_for_model(Review)
			tmp_photo.object_id = review.pk
			tmp_photo.restaurant_id = review.restaurant.pk
			tmp_photo.user = review.user
			tmp_photo.save()
			review.photo = tmp_photo
			review.save()

		request.content_object = review.restaurant

		review_item = render_to_string('inc_review_single.html', {
			'pk': review.pk,
			'username':review.user.get_full_name(),
			'review':review,
			'restaurant':review.restaurant,
		}, context_instance=RequestContext(request))

		response = {
			'status' : 1,
			'html' : review_item,
			'msg' : '',
		}

		return HttpResponse(json.dumps(response), mimetype="application/json")

	else :
		response = {
			'status' : 0,
			'html' : '',
			'msg' : form.errors,
		}
		return HttpResponse(json.dumps(response), mimetype="application/json")

def review_more(request):
	items_per_page = 5
	enc_sid = request.POST.get('sid', None)
	sid = Review.objects.sid_source(enc_sid)
	owner = request.POST.get('owner', None)

	all_reviews = Review.objects.filter(restaurant=owner, created__lt=sid['created']).order_by('-created')
	total_items = all_reviews.count()
	html_str = ''
	if total_items > 0:
		show_reviews = all_reviews[:items_per_page]
		for review in show_reviews:
			html_str = html_str + render_to_string('inc_review_single.html', {
				'review':review,
				'restaurant':review.restaurant,
			}, context_instance=RequestContext(request))
	data = {
		'more':(total_items > items_per_page),
		'html':html_str,
	}
	return HttpResponse(json.dumps(data), mimetype="application/json")
