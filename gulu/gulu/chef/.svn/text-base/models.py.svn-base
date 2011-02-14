""" Gulu chef module models """

import datetime

from django.db import models


class Chef(models.Model):
    restaurant      = models.ForeignKey('restaurant.Restaurant', related_name = "chefs")    
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    points          = models.IntegerField(default=0)
    created         = models.DateTimeField(default=datetime.datetime.now)
    #type            = models.ForeignKey('ChefType')
    #user            = models.ForeignKey('user_profiles.UserProfile')    
    #photo
        
    def __unicode__(self):
        return self.name