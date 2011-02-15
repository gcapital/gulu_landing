""" Gulu restaurant module admin definitions """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 549 2011-01-19 05:37:26Z gage $"

from django.contrib import admin
from restaurant.models import *
from photos.admin import GenericPhotoInline

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'slug', 'city', 'region', 'created')
	inlines = [GenericPhotoInline,]

	
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantType)
admin.site.register(Chef)
admin.site.register(RestaurantRating)
admin.site.register(Vip)
admin.site.register(RestaurantService)