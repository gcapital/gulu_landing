""" Gulu mission module views """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: views.py 404 2010-12-17 03:32:45Z de $"

import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings

from mission.models import Mission

def index(request):
    
    return render_to_response('mission_index.html', {
        'missions'        : Mission.objects
                                .filter(
                                    start_time__lte=datetime.datetime.now,
                                    end_time__gte=datetime.datetime.now,
                                    active=True,
                                    is_sponsor=False,
                                    )
                                .order_by('end_time'),
        'sponsor_missions': Mission.objects
                                .filter(
                                    start_time__lte=datetime.datetime.now,
                                    end_time__gte=datetime.datetime.now,
                                    active=True,
                                    is_sponsor=True,
                                    )
                                .order_by('end_time'),
    }, context_instance = RequestContext(request))
