from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from landing.forms import RegistrationForm
from landing.models import Registration

def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks for signing up.  We'll let you know when the beta " \
                "is available")
    else:
        form = RegistrationForm()
    
    return render_to_response("landing_index.html", {
        'form': form,
    }, context_instance=RequestContext(request))