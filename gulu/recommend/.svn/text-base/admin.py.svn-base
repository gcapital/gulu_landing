""" Gulu recommend module admin definitions """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: admin.py 388 2010-12-16 06:59:01Z ben $"

from django.contrib import admin
from recommend.models import RestaurantRecommend, DishRecommend

class RestaurantRecommendAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'created_user', 'created')
    
class DishRecommendAdmin(admin.ModelAdmin):
    list_display = ('dish', 'created_user', 'created')

admin.site.register(RestaurantRecommend, RestaurantRecommendAdmin)
admin.site.register(DishRecommend, DishRecommendAdmin)


