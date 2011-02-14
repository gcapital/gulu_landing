""" Deal admin configuration """

__author__ = "Jason Ke <u912538@gmail.com>"
__version__ = "$Id: admin.py$"

from django.contrib import admin
from deal.models import Deal

class DealAdmin(admin.ModelAdmin):
    """ Deal admin class """
    list_display = ('pk', 'restaurant', 'title', 'type', 'amount', 'dish', 'start_datetime', 'end_datetime', 'ongoing', 'conditions', 'cover')
    list_filter = []
    list_per_page = 10

admin.site.register(Deal, DealAdmin)