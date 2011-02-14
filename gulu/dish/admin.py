""" Dish admin configuration """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: admin.py 549 2011-01-19 05:37:26Z gage $"

from django.contrib import admin

from dish.models import Dish, DishType, DishRanking
from photos.admin import GenericPhotoInline

class DishAdmin(admin.ModelAdmin):
    """ Dish admin class """
    list_display = ('pk', 'name', 'created', 'price', 'vip_price', 'type', 'restaurant', 'special', 'active')
    list_filter = ['created']
    list_per_page = 10
    inlines = [GenericPhotoInline,]

class DishRankingAdmin(admin.ModelAdmin):
    """ Dish DishRanking class """
    list_display = ('dish', 'rank', 'created')
    list_filter = ['created']
    list_per_page = 10
    
admin.site.register(Dish, DishAdmin)
admin.site.register(DishType)
admin.site.register(DishRanking)