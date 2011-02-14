""" Gulu recommend module models """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id$"

import datetime

from django.db import models

class BaseRecommend(models.Model):
    created_user    = models.ForeignKey('user_profiles.UserProfile')
    score           = models.IntegerField(default=0)
    created         = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.created_user
    
    class Meta:
        abstract    = True
        ordering    = ['-score']

class RestaurantRecommend(BaseRecommend):
    restaurant      = models.ForeignKey('restaurant.Restaurant')
    
    def __unicode__(self):
        return self.restaurant.name
    
class DishRecommend(BaseRecommend):
    dish            = models.ForeignKey('dish.Dish')
    
    def __unicode__(self):
        return self.dish.name
    
