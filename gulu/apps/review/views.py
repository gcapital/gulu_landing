# Create your views here.
""" Gulu invite module views """
__author__ = "Jason Ke <u912538@gmail.com>"
__version__ = "$Id: views.py 588 2011-01-27 05:50:54Z peter $"

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings

from review.forms import CreateReviewForm
from review.models import Review
#from photos.models import DishPhoto
from restaurant.models import Restaurant, RestaurantService
from user_profiles.models import UserProfile


def view_index(request, restaurant_id):
    items_per_page = 5
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
    else:
        form = CreateReviewForm(initial={'restaurant': restaurant_id, 'user':request.user})
    all_reviews = Review.objects.filter(restaurant=restaurant_id).order_by('-created')

    return render_to_response('review-view-index.html', {
        'best_review': Review.objects.filter(restaurant=restaurant_id)[:1][0],
        'most_helpful_favorite_review': Review.objects.filter(restaurant=restaurant_id)[:1][0],
        'most_helpful_critical_review': Review.objects.filter(restaurant=restaurant_id)[:1][0],
        #'best_photos': DishPhoto.objects.all(),
        #'best_videos': DishPhoto.objects.all(),
        'restaurant': Restaurant.objects.get(pk=restaurant_id),
        'all_reviews': all_reviews[:items_per_page],
        'more_review_button': (all_reviews.count() > items_per_page),
        'services' : RestaurantService.objects.all(),
        'form': form,
    }, context_instance=RequestContext(request))

def user_view_index(request, user_id):
    user_profile = get_object_or_404(UserProfile, pk=user_id)

    return render_to_response('review_user_view_index.html', {
        'current_user': request.user,
        'all_reviews': Review.objects.filter(user=user_id),
        'user_profile': user_profile,
    }, context_instance=RequestContext(request))

def view_detail(request, restaurant_id, review_id):
    return render_to_response('review-view-detail.html', {
        'review': Review.objects.get(pk=review_id),
        'restaurant' : Restaurant.objects.get(pk=restaurant_id),
        'services' : RestaurantService.objects.all(),
    }, context_instance=RequestContext(request))

def user_view_detail(request, user_id, review_id):
    user_profile = get_object_or_404(UserProfile, pk=user_id)

    return render_to_response('review_user_view_detail.html', {
        'current_user': request.user,
        'review': Review.objects.get(pk=review_id),
        'user_profile': user_profile,
    }, context_instance=RequestContext(request))

