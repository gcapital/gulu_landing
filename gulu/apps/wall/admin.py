""" Photos admin configuration """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 549 2011-01-19 05:37:26Z gage $"

from django.contrib import admin

from wall.models import *

class WallPostAdmin(admin.ModelAdmin):
	""" wall admin class """
	
	#list_display = ('pk', 'poster', 'content', 'create_time', 'update_time')
	list_per_page = 10

admin.site.register(WallPost, WallPostAdmin)
