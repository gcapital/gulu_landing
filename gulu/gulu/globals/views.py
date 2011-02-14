""" Gulu globals module views """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: views.py 554 2011-01-20 09:44:15Z ben $"

from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django import http
from django.contrib.auth.decorators import login_required

from globals.forms import SignupForm
from globals.utils import slugreverse
from user_profiles.models import UserProfile

from restaurant.models import Restaurant


def handler403(request):
	""" 403 handler """
	t = loader.get_template('403.html')
	return http.HttpResponseForbidden(t.render(RequestContext(request)))
	
def handler404(request):
    """ gulu home page """

    t = loader.get_template('404.html')
    return http.HttpResponseNotFound(t.render(RequestContext(request, 
      {'request_path': request.path,})))

def handler500(request):
    """ gulu home page """

    t = loader.get_template('500.html')
    return http.HttpResponseServerError(t.render(RequestContext(request, 
      {'request_path': request.path,})))

def home(request):
    """ gulu home page """
    slidephotos = []
    #slidephotos = DishPhoto.objects.filter(dish__restaurant=1)[:4]
    tmp_restaurant = Restaurant.objects.get(pk=1)
    return render_to_response('home_index.html', { 'slidephotos':slidephotos, 'tmp_restaurant':tmp_restaurant }, context_instance = RequestContext(request))
    
def signup(request):
	
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			data = form.save(commit = False)
			new_user = UserProfile.objects.create_user(data.email, data.email, data.password)
			new_user.save()
			return redirect("globals-login")
	else:
		form = SignupForm()
	
	return render_to_response("globals_signup.html", {
		'form': form,
	}, context_instance=RequestContext(request))

@login_required
def logged_in(request):
	next = request.GET.get('next')
	if next:
		return HttpResponseRedirect(next)
	
	return HttpResponseRedirect(slugreverse(request.user, "user-profile", args=[request.user.id]))
	
def logout(request):
	pass
	
def forgot_password(request):
	pass
