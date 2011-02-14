import datetime

from django.db import models

class Event(models.Model):
    date                = models.BigIntegerField()
    title               = models.CharField(max_length=50, null=True, blank=True)
    user                = models.ForeignKey('user_profiles.UserProfile')
    restaurant          = models.ForeignKey('restaurant.Restaurant')
    
    def __unicode__(self):
        return self.title;

    
