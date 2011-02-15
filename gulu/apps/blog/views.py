""" Gulu blog module views """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: views.py 571 2011-01-26 07:50:47Z ben $"

from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from actstream import action
from restaurant.models import Restaurant
from blog.models import RestaurantPost, UserPost
from blog.forms import AddEditRestaurantPostForm, AddEditUserPostForm
from globals.utils import slugreverse
from user_profiles.models import UserProfile

def restaurant_posts(request, restaurant_id):
	""" Restaurant blog posts index view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render_to_response('blog_restaurant_posts.html', {
		'restaurant': restaurant,
	}, context_instance = RequestContext(request))
	
def restaurant_view_post(request, restaurant_id, post_id):
	""" Restaurant blog post detail view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	post = get_object_or_404(RestaurantPost, restaurant=restaurant, pk=post_id)
	
	return render_to_response('blog_restaurant_view_post.html', {
		'restaurant': restaurant,
		'post': post,
	}, context_instance = RequestContext(request))

@login_required
def restaurant_add_post(request, restaurant_id):
	""" Restaurant blog add post view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	
	if request.method == 'POST':
		form = AddEditRestaurantPostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.poster = request.user
			post.restaurant = restaurant
			post.save()
			return HttpResponseRedirect(slugreverse(restaurant, "restaurant-view-post", args=[restaurant.id, post.id]))
	else:
		form = AddEditRestaurantPostForm()
		
	return render_to_response('blog_restaurant_add_post.html', {
		'restaurant': restaurant,
		'form': form,
	}, context_instance = RequestContext(request))

@login_required	
def restaurant_edit_post(request, restaurant_id, post_id):
	""" Restaurant blog edit post view """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	post = get_object_or_404(RestaurantPost, restaurant=restaurant, pk=post_id)
	
	if request.method == 'POST':
		form = AddEditRestaurantPostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(slugreverse(restaurant, "restaurant-view-post", args=[restaurant.id, post.id]))	
	else:
		form = AddEditRestaurantPostForm(instance=post)
	
	return render_to_response('blog_restaurant_edit_post.html', {
		'restaurant': restaurant,
		'post': post,
		'form': form,
	}, context_instance = RequestContext(request))

def user_posts(request, user_id):
	""" User blog posts index view """
	
	user_profile = get_object_or_404(UserProfile, pk=user_id)
	
	return render_to_response('blog_user_posts.html', {
		'user_profile': user_profile,
	}, context_instance = RequestContext(request))
	
def user_view_post(request, user_id, post_id):
	""" User blog post detail view """
	
	user_profile = get_object_or_404(UserProfile, pk=user_id)
	post = get_object_or_404(UserPost, owner=user_profile, pk=post_id)
	
	return render_to_response('blog_user_view_post.html', {
		'user_profile': user_profile,
		'post': post,
	}, context_instance = RequestContext(request))

@login_required
def user_add_post(request, user_id):
	""" User blog add post view """
	
	user_profile = get_object_or_404(UserProfile, pk=user_id)
	
	if request.method == 'POST':
		form = AddEditUserPostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.poster = request.user
			post.owner = user_profile
			post.save()
			
			# send the activity stream action signal
			action.send(request.user, verb="wrote a blog post", target=post)
			
			return HttpResponseRedirect(slugreverse(user_profile, "user-view-post", args=[user_profile.id, post.id]))
	else:
		form = AddEditUserPostForm()
		
	return render_to_response('blog_user_add_post.html', {
		'user_profile': user_profile,
		'form': form,
	}, context_instance = RequestContext(request))

@login_required	
def user_edit_post(request, user_id, post_id):
	""" User blog edit post view """
	
	user_profile = get_object_or_404(UserProfile, pk=user_id)
	post = get_object_or_404(UserPost, owner=user_profile, pk=post_id)
	
	if request.method == 'POST':
		form = AddEditUserPostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(slugreverse(user_profile, "user-view-post", args=[user_profile.id, post.id]))	
	else:
		form = AddEditUserPostForm(instance=post)
	
	return render_to_response('blog_user_edit_post.html', {
		'user_profile': user_profile,
		'post': post,
		'form': form,
	}, context_instance = RequestContext(request))
