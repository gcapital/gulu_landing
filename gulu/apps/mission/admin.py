""" Gulu mission module admin definitions """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: admin.py 388 2010-12-16 06:59:01Z ben $"

from django.contrib import admin
from mission.models import Mission

admin.site.register(Mission)

