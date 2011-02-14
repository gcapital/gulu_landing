""" Gulu mission module models """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id: models.py 534 2011-01-11 04:20:28Z ben $"

import datetime

from django.db import models

class Mission(models.Model):
    restaurants     = models.ManyToManyField('restaurant.Restaurant')
    dishes          = models.ManyToManyField('dish.Dish', null=True, blank=True)
    created_user    = models.ForeignKey('user_profiles.UserProfile')
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    is_sponsor      = models.BooleanField()
    start_time      = models.DateTimeField(default=datetime.datetime.now) # mission start time
    end_time        = models.DateTimeField(default=datetime.datetime.now) # mission end time 
    reward_point    = models.PositiveIntegerField(default=0) #
    user_limit      = models.PositiveIntegerField(default=0) # limitation of join count, 0 means no limit
    area            = models.CharField(max_length=50, blank=True, null=True) #
    cross_location  = models.BooleanField(default=False) # for group mission 
    join_count      = models.PositiveIntegerField(default=0) #
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.name
