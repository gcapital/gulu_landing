""" Photos admin configuration """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 549 2011-01-19 05:37:26Z gage $"

from django.contrib import admin
from django.contrib.contenttypes import generic

from photos.models import *

class GenericPhotoInline(generic.GenericTabularInline):
    model = Photo
    #fields = []

class PhotoAdmin(admin.ModelAdmin):
	""" Base photo admin class """
	list_display = ('pk', 'title', 'user', 'restaurant_id', 'content_type', 'object_id', 'content_object', 'is_main', 'is_featured', 'order', 'view_count', 'created', 'admin_thumbnail_view')
	list_filter = ['created', 'content_type']
	list_per_page = 10

admin.site.register(Photo, PhotoAdmin)