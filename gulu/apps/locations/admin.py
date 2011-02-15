""" Gulu other locations module admin definitions """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 388 2010-12-16 06:59:01Z ben $"

from django.contrib import admin

from locations.models import *

class OtherLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_restaurant', 'to_restaurant', 'added',)


class OtherLocationInvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_restaurant', 'to_restaurant', 'sent', 'status',)


admin.site.register(OtherLocation, OtherLocationAdmin)
admin.site.register(OtherLocationInvitation, OtherLocationInvitationAdmin)
