""" Gulu dish module models """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: models.py 549 2011-01-19 05:37:26Z gage $"

import datetime

from django.db import models

class Dish(models.Model):
    restaurant      = models.ForeignKey('restaurant.Restaurant', related_name = "dishes")
    user            = models.ForeignKey('user_profiles.UserProfile')
    name            = models.CharField(max_length=100)
    vip_price       = models.FloatField(default=0)
    price           = models.FloatField(default=0)
    description     = models.TextField()
    dish_pics       = models.ManyToManyField('photos.Photo', related_name='%(app_label)s_%(class)s_related_dish', null=True, blank=True)
    main_pic        = models.ForeignKey('photos.Photo', related_name='%(app_label)s_%(class)s_main_pic_dish', null=True, blank=True)
    type            = models.ForeignKey('DishType')
    points          = models.IntegerField(default=0)
    reserve         = models.BooleanField(default=True)
    total_reserve   = models.IntegerField(default=0)
    sale_out        = models.BooleanField(default=False)
    special         = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(default=datetime.datetime.now)
    count_recommend        = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

class DishType(models.Model):
    name        = models.CharField(max_length=100)
    restaurant  = models.ForeignKey('restaurant.Restaurant')
    is_default  = models.BooleanField(default=False)
    created     = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.name

class DishRanking(models.Model):
    dish        = models.ForeignKey('Dish')
    rank        = models.PositiveIntegerField()
    created     = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.dish