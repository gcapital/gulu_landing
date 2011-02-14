from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from restaurant.models import Restaurant
from globals.utils import slugreverse
from chef.models import Chef
from chef.forms import AddEditChefForm
#from review.forms import CreateReviewForm
#from review.models import Review


def view_chef(request, restaurant_id):
    """ Shows chefs in a particular restaurant """
    
    chefs = Chef.objects.filter(restaurant=restaurant_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        
    return render_to_response('chef_view_chef.html', {
        'chefs'  : chefs,
        'restaurant' : restaurant,
    }, context_instance = RequestContext(request))


@login_required
def add_chef(request, restaurant_id):
    """ Adds chefs in a particular restaurant """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)    
    if request.method == 'POST':
        form = AddEditChefForm(request.POST)
        if form.is_valid():
            chef = form.save(commit=False)
            chef.restaurant = restaurant
            chef.save()
            return HttpResponseRedirect(slugreverse(restaurant, "restaurant-chef", args=[restaurant.id,]))
    else:
        form = AddEditChefForm()

     
    return render_to_response('chef_add_chef.html', {
        'restaurant' : restaurant,
        'form' : form,
    }, context_instance = RequestContext(request))
    
    
