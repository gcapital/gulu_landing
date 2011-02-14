""" Gulu dish module views """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: views.py 553 2011-01-20 09:13:33Z ben $"

from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from guardian.decorators import permission_required_or_403

from restaurant.models import Restaurant, RestaurantService
from globals.utils import slugreverse
from dish.models import Dish, DishType
from dish.forms import AddEditDishForm
from review.forms import CreateReviewForm
from review.models import Review

def menu(request, restaurant_id):
    """ Shows all dishes at a particular restaurant """
    
    dishes = Dish.objects.filter(restaurant=restaurant_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    menu_list_html = render_to_string('inc_menu_list.html',{
         'dishes': dishes,
         'restaurant' : restaurant,
    }, context_instance = RequestContext(request))
    
    return render_to_response('dish_menu.html', {
        'dishes'  : dishes,
        'dishtypes' : DishType.objects.filter(restaurant=restaurant_id),
        'restaurant' : restaurant,
        'menu_list_html' : menu_list_html,
    }, context_instance = RequestContext(request))

def view_dish(request, restaurant_id, dish_id):
    """ Show details of a particular dish """
    
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    dish = Dish.objects.get(restaurant=restaurant, pk=dish_id,)
    all_reviews = Review.objects.filter(restaurant=restaurant, dish=dish)
    
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
    else:
        form = CreateReviewForm()
	
	return render_to_response('dish_view_dish.html', {
        'restaurant': restaurant,
        'dish': dish,
        'all_reviews': all_reviews,
        'form': form,
        'current_user': request.user,
    }, context_instance = RequestContext(request))
   
@permission_required_or_403('restaurant.manage_restaurant',
	(Restaurant, 'pk', 'restaurant_id'))
def add_dish(request, restaurant_id):
    """ Add a dish """
    
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    dishes = Dish.objects.filter(restaurant=restaurant)
    #photos = DishPhoto.objects.filter(dish__restaurant=restaurant_id)
    
    if request.method == "POST":
		form = AddEditDishForm(request.POST)
		if form.is_valid():
			dish = form.save(commit=False)
			dish.restaurant = restaurant
			dish.user = request.user
			dish.save()
			return HttpResponseRedirect(slugreverse(restaurant, "restaurant-view-dish", args=[restaurant.id, dish.id]))
    else:
		form = AddEditDishForm()
	
    return render_to_response('dish_add_dish.html', {
        'restaurant': restaurant,
        #'photos': photos,
        'dishes': dishes,
        'form': form,
    }, context_instance = RequestContext(request))

@permission_required_or_403('restaurant.manage_restaurant',
	(Restaurant, 'pk', 'restaurant_id'))
def edit_dish(request, restaurant_id, dish_id):
	""" Edit a dish """
	
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	dish = get_object_or_404(Dish, restaurant=restaurant, pk=dish_id)
	
	if request.method == "POST":
		form = AddEditDishForm(request.POST, instance=dish)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(slugreverse(restaurant, "restaurant-view-dish", args=[restaurant.id, dish.id]))
	
	else:
		form = AddEditDishForm(instance=dish)
	
	return render_to_response('dish_edit_dish.html', {
        'restaurant': restaurant,
        'dish': dish,
        'form': form,
    }, context_instance = RequestContext(request))
    
